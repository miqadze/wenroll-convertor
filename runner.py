from flask import Flask, request, make_response
import subprocess
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['PUT'])
def handle_request():
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return "Error: Authorization token missing", 401

    if 'video_key' in request.args and 'file' in request.files:
        video_key = request.args['video_key']
        file = request.files['file']
        # validate token
        validate_token_response = requests.post('apitest.wenroll.com/validateToken', headers={'Authorization': auth_token})
        if validate_token_response.status_code != 200:
            return "Error: Token validation failed", validate_token_response.status_code

        file.save(video_key)
        subprocess.Popen(["/usr/bin/python3", "convert.py", video_key])
        response = make_response("Process started", 200)
        return response
    else:
        return "Error: Invalid request", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
