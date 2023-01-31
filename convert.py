import sys
import os
import subprocess
import boto3
import time
input_file = sys.argv[1]
folder_name = input_file.rsplit(".", 1)[0]
output_file = folder_name + '_compressed.mp4'
thumbnail_file = folder_name + "_thumbnail.jpg"
try:
   start = time.perf_counter()
   subprocess.run(["/usr/bin/ffmpeg", "-i", input_file, "-vframes", "1", "-ss", "00:00:01", "-y", thumbnail_file])
   elapsed_time = time.perf_counter() - start
   with open('py.log', 'a') as f:
       f.write(f"Time spent on taking thumbnail: {elapsed_time:0.2f} seconds\n")
except Exception as e:
   print(f"Error occured while running jpeg generation: {e}")
s3 = boto3.client('s3')
try:
    s3.upload_file(folder_name + "_thumbnail.jpg", "production-wenroll", folder_name + "/" + folder_name + "_thumbnail.jpg")
except Exception as e:
    print(f"Error occurred while running upload_file(jpeg) on Production with error: {e}")
try:
    start = time.perf_counter()
    subprocess.run(['/usr/bin/ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-crf', '25', '-preset', 'medium', '-tune', 'film', '-threads', '32', '-y', output_file])
    with open('py.log', 'a') as f:
       f.write(f"Time spent on compressing video: {elapsed_time:0.2f} seconds\n")
except Exception as e:
    print(f"Error occurred while running ffmpeg: {e}")
try:
    subprocess.run(["/usr/bin/ffmpeg", "-i", output_file, "-s", "hd720", folder_name + "_720p.mp4"])
    subprocess.run(["/usr/bin/ffmpeg", "-i", output_file, "-s", "hd480", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_480p.m3u8"])
    subprocess.run(["/usr/bin/ffmpeg", "-i", output_file, "-s", "hd720", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_720p.m3u8"])
    subprocess.run(["/usr/bin/ffmpeg", "-i", output_file, "-s", "hd1080", "-hls_time", "10", "-hls_flags", "single_file", "-hls_list_size", "0", "-f", "hls", folder_name + "_1080p.m3u8"])
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
os.chmod(folder_name + "_720p.mp4", 0o777)
os.chmod(folder_name + "_480p.ts", 0o777)
os.chmod(folder_name + "_720p.ts", 0o777)
os.chmod(folder_name + "_1080p.ts", 0o777)
os.chmod(folder_name + "_480p.m3u8", 0o777)
os.chmod(folder_name + "_720p.m3u8", 0o777)
os.chmod(folder_name + "_1080p.m3u8", 0o777)
os.chmod(folder_name + "_playlist.m3u8", 0o777)
os.chown(folder_name + "_720p.mp4", 1000, 1000)
os.chown(folder_name + "_480p.ts", 1000, 1000)
os.chown(folder_name + "_720p.ts", 1000, 1000)
os.chown(folder_name + "_1080p.ts", 1000, 1000)
os.chown(folder_name + "_480p.m3u8", 1000, 1000)
os.chown(folder_name + "_720p.m3u8", 1000, 1000)
os.chown(folder_name + "_1080p.m3u8", 1000, 1000)
os.chown(folder_name + "_playlist.m3u8", 1000, 1000)
with open('py.log', 'a') as f:
    subprocess.run(['/usr/bin/python3', 's3.py', folder_name], stdout=f)