from flask import Flask, request, make_response
import subprocess
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def check_authorization(get_response):
    def middleware(request):
        auth_header = request.headers.get("Authorization")
        video_key = request.args['video_key']
        if not auth_header:
            return "Unauthorized", 401
        headers = {"Authorization": auth_header, "video_key":video_key}
        response = requests.post("https://apitest.wenroll.com/validate", headers=headers)
        if response.status_code != 200:
            return "Unauthorized", 401
        response = get_response(request)
        return response
    return middleware
app.wsgi_app = check_authorization(app.wsgi_app)


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
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)