from importlib import import_module
import os
import cv2
import sys
from flask import Flask, render_template, send_file, Response
from flask_restful import Resource, Api

# import camera driver
# if os.environ.get('CAMERA'):
#     Camera = import_module('camera_' + os.environ['CAMERA']).Camera
# else:
#     from camera import Camera

from camera_opencv import Camera


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

api = Api(app)


@app.route('/')
def index():
    return render_template('sanBerryStream.html')

@app.route('/resources')
@app.route('/resources/<name>')
def resource(name=None):
    ext = os.path.splitext(name)[1]
    return send_file("resources/" + name, mimetype='image/%s' % ext)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
