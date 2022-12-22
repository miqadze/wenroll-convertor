import sys
import os
import subprocess
import boto3

input_file = sys.argv[1]
folder_name = input_file.rsplit(".", 1)[0]
output_file = folder_name + '_compressed.mp4'

try:
    subprocess.run(['ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-crf', '20', '-y', output_file])
except Exception as e:
    print(f"Error occurred while running ffmpeg: {e}")

try:
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd480", folder_name + "_480p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd720", folder_name + "_720p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd1080", folder_name + "_1080p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_list_size", "0", "-f", "hls", folder_name + "_480p.m3u8"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_list_size", "0", "-f", "hls", folder_name + "_720p.m3u8"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_list_size", "0", "-f", "hls", folder_name + "_1080p.m3u8"])
except Exception as e:
    print(f"Error occurred while running ffmpeg: {e}")

playlist = "#EXTM3U\n"
playlist += "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=200000\n"
playlist += folder_name + "_480p.m3u8\n"
playlist += "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000\n"
playlist += folder_name + "_720p.m3u8\n"
playlist += "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000\n"
playlist += folder_name + "_1080p.m3u8\n"

with open(folder_name + "_playlist.m3u8", "w") as f:
    f.write(playlist)

os.chmod(folder_name + "_480p.mp4", 0o777)
os.chmod(folder_name + "_720p.mp4", 0o777)
os.chmod(folder_name + "_1080p.mp4", 0o777)
os.chmod(folder_name + "_playlist.m3u8", 0o777)

s3 = boto3.client("s3")

try:
    s3.upload_file(folder_name + "_480p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_480p.mp4")
    s3.upload_file(folder_name + "_720p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_720p.mp4")
    s3.upload_file(folder_name + "_1080p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_1080p.mp4")
    s3.upload_file(folder_name + "_480p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_480p.m3u8")
    s3.upload_file(folder_name + "_720p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_720p.m3u8")
    s3.upload_file(folder_name + "_1080p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_1080p.m3u8")
    s3.upload_file(folder_name + "_480p0.ts", "test-wenroll", folder_name + "/" + folder_name + "_480p0.ts")
    s3.upload_file(folder_name + "_720p0.ts", "test-wenroll", folder_name + "/" + folder_name + "_720p0.ts")
    s3.upload_file(folder_name + "_1080p0.ts", "test-wenroll", folder_name + "/" + folder_name + "_1080p0.ts")
    s3.upload_file(folder_name + "_480p1.ts", "test-wenroll", folder_name + "/" + folder_name + "_480p0.ts")
    s3.upload_file(folder_name + "_720p1.ts", "test-wenroll", folder_name + "/" + folder_name + "_720p0.ts")
    s3.upload_file(folder_name + "_1080p1.ts", "test-wenroll", folder_name + "/" + folder_name + "_1080p0.ts")
    s3.upload_file(folder_name + "_playlist.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_playlist.m3u8")
except Exception as e:
    print(f"Error occurred while running upload_file: {e}")


os.remove(folder_name + "_480p.mp4")
os.remove(folder_name + "_720p.mp4")
os.remove(folder_name + "_1080p.mp4")
os.remove(folder_name + "_playlist.m3u8")