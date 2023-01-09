from flask import Flask, request
import subprocess
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    if 'video_key' in request.form and 'file' in request.files:
        video_key = request.form['video_key']
        file = request.files['file']
        file.save(video_key)
        subprocess.Popen(["/usr/bin/python3", "convert.py", video_key])
        return "Process started", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')