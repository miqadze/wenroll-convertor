import sys
import os
import subprocess
import boto3

input_file = sys.argv[1]
folder_name = input_file.rsplit(".", 1)[0]
output_file = folder_name + '_compressed.mp4'

try:
    subprocess.run(['ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-crf', '25', '-preset', 'medium', '-tune', 'film', '-y', output_file])
except Exception as e:
    print(f"Error occurred while running ffmpeg: {e}")

try:
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd480", folder_name + "_480p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd720", folder_name + "_720p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-s", "hd1080", folder_name + "_1080p.mp4"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_480p.m3u8"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_720p.m3u8"])
    subprocess.run(["ffmpeg", "-i", output_file, "-codec:", "copy", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_1080p.m3u8"])
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
os.chmod(folder_name + "_480p.ts", 0o777)
os.chmod(folder_name + "_720p.ts", 0o777)
os.chmod(folder_name + "_1080p.ts", 0o777)
os.chmod(folder_name + "_480p.m3u8", 0o777)
os.chmod(folder_name + "_720p.m3u8", 0o777)
os.chmod(folder_name + "_1080p.m3u8", 0o777)
os.chmod(folder_name + "_playlist.m3u8", 0o777)

os.chown(folder_name + "_480p.mp4", 1000, 1000)
os.chown(folder_name + "_720p.mp4", 1000, 1000)
os.chown(folder_name + "_1080p.mp4", 1000, 1000)
os.chown(folder_name + "_480p.ts", 1000, 1000)
os.chown(folder_name + "_720p.ts", 1000, 1000)
os.chown(folder_name + "_1080p.ts", 1000, 1000)
os.chown(folder_name + "_480p.m3u8", 1000, 1000)
os.chown(folder_name + "_720p.m3u8", 1000, 1000)
os.chown(folder_name + "_1080p.m3u8", 1000, 1000)
os.chown(folder_name + "_playlist.m3u8", 1000, 1000)
with open("py.log", "w") as log_file:
    subprocess.run(["python3", "s3.py", folder_name], stdout=log_file, stderr=log_file)
