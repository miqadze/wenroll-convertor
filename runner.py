from flask import Flask, request, Request, Response, make_response
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

class CheckAuthorization(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        auth_header = request.headers.get("Authorization")
        video_key = request.args['video_key']

        print("Authorizatin Header", auth_header)

        if auth_header is None:
            res = Response(u'Unauthorized', mimetype='text/plain', status=401)
            print(res)
            return res(environ, start_response)

        headers = {"Authorization": auth_header, 'videoKey': video_key}
        response = requests.post(
            "https://apitest.wenroll.com/auth/validateToken", headers=headers)

        response_data = response.json()

        print("Token validation response", response_data)

        if response_data['statusCode'] != 200:
            res = Response(u'Unauthorized', mimetype='text/plain', status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)
app.wsgi_app = CheckAuthorization(app.wsgi_app)

@app.route('/', methods=['PUT'])
def handle_request():
    if 'video_key' in request.args and 'file' in request.files:
        video_key = request.args['video_key']

        file = request.files['file']
        file.save(video_key)
        subprocess.Popen(["/usr/bin/python3", "convert.py", video_key])
        response = make_response("Process started", 200)
        return response
    else:
        return "Error: Invalid request", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)