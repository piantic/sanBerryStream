from importlib import import_module
import os
import cv2
import sys
from flask import Flask, render_template, send_file, Response, redirect, jsonify
from flask_restful import Resource, Api
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

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

status = "bad"

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    sanBerryStatus = String(name=String(default_value="Good"))
    goodbye = String()

    def resolve_hello(self, info, name):
        if name == "jerry":
            return f'{name} is god.'
        return f'Hello {name}!'

    def resolve_goodbye(self, info):
        return 'See ya!'

    def resolve_sanBerryStatus(self, info, name):
        if name == "San":
            return f"{name} is good."
        elif name == "check":
            return status
        elif name == "jerry":
            return f"{name} is god."
        return f'Hello {name}!'


schema = Schema(query=Query)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        '/graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def index():
    return redirect('/page/sanBerryStream.html')


@app.route('/favicon.ico')
def favicon():
    return ""


@app.route('/datInfo')
@app.route('/datInfo/<query>')
def datInfo(query=None):
    #queryString = '{ hello }'
    # queryString = '{ hello(name: "Jerry") }'
    # result = schema.execute(queryString)
    # print(result.data['hello'])
    print(query)
    result = schema.execute(query)
    return jsonify(result.data)


@app.route('/page')
@app.route('/page/<name>')
def page(name=None):
    error = "Page Error"
    return render_template(name, error=error)


@app.route('/resources')
@app.route('/resources/<name>')
def resource(name=None):
    ext = os.path.splitext(name)[1]
    print(os.path.splitext(name))
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
