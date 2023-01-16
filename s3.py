import sys
import boto3
import os
import pymongo
import subprocess
import requests
folder_name = sys.argv[1]
s3 = boto3.client('s3')
bucket_name = "production-wenroll"
try:
 #   s3.upload_file(folder_name + "_480p.mp4", bucket_name, folder_name + "/" + folder_name + "_480p.mp4")
    s3.upload_file(folder_name + "_720p.mp4", bucket_name, folder_name + "/" + folder_name + "_720p.mp4")
 #   s3.upload_file(folder_name + "_1080p.mp4", bucket_name, folder_name + "/" + folder_name + "_1080p.mp4")
    s3.upload_file(folder_name + "_480p.m3u8", bucket_name, folder_name + "/" + folder_name + "_480p.m3u8")
    s3.upload_file(folder_name + "_720p.m3u8", bucket_name, folder_name + "/" + folder_name + "_720p.m3u8")
    s3.upload_file(folder_name + "_1080p.m3u8", bucket_name, folder_name + "/" + folder_name + "_1080p.m3u8")
    s3.upload_file(folder_name + "_480p.ts", bucket_name, folder_name + "/" + folder_name + "_480p.ts")
    s3.upload_file(folder_name + "_720p.ts", bucket_name, folder_name + "/" + folder_name + "_720p.ts")
    s3.upload_file(folder_name + "_1080p.ts", bucket_name, folder_name + "/" + folder_name + "_1080p.ts")
    s3.upload_file(folder_name + "_playlist.m3u8", bucket_name, folder_name + "/" + folder_name + "_playlist.m3u8")
    s3.upload_file(folder_name + "_compressed.mp4", bucket_name, folder_name + "/" + folder_name + ".mp4")
except Exception as e:
    print(f"Error occurred while running upload_file: {e}")
try:
    url = "https://api.wenroll.com/videos/conversion-success"
    data = {"videoKey": folder_name + ".mp4"}
    response = requests.put(url, json=data)
    if response.status_code != 200:
        print(f"Error occurred while sending PUT request: {response.text}")
except Exception as e:
    print(f"Error occured while writing in database: {e}")
#os.remove(folder_name + "_480p.mp4")
os.remove(folder_name + "_720p.mp4")
#os.remove(folder_name + "_1080p.mp4")
os.remove(folder_name + "_playlist.m3u8")
os.remove(folder_name + "_480p.m3u8")
os.remove(folder_name + "_720p.m3u8")
os.remove(folder_name + "_1080p.m3u8")
os.remove(folder_name + "_480p.ts")
os.remove(folder_name + "_720p.ts")
os.remove(folder_name + "_1080p.ts")
os.remove(folder_name + ".mp4")
os.remove(folder_name + "_compressed.mp4")
os.remove(folder_name + "_thumbnail.jpg")