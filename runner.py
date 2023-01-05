from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    if 'video_name' in request.args:
        video_name = request.args['video_name']
        bucket_name = "production-wenroll"
        url = "https://s3.eu-central-1.amazonaws.com/{}/{}".format(bucket_name, video_name)
        content = requests.get(url).content
        if content is None:
            return "Error: File not found", 404
        else:
            with open(video_name, 'wb') as f:
                f.write(content)
            subprocess.run(["python3", "convert.py", video_name])
            return "Process started", 200
#test
if __name__ == '__main__':
    app.run(host='0.0.0.0')
