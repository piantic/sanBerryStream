import os
import cv2
import sys
from flask import Flask, render_template, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

api = Api(app)

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world1'}

camera = cv2.VideoCapture(0)


@app.route('/')
def index():
    return render_template('sanBerryStream.html')

@app.route('/resources')
@app.route('/resources/<name>')
def resource(name=None):
    ext = os.path.splitext(name)[1]
    return send_file("resources/" + name, mimetype='image/%s' % ext)


def video()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
