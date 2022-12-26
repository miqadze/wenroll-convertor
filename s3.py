import sys
import boto3
import os

folder_name = sys.argv[1]

s3 = boto3.client('s3', region_name='eu-central-1', aws_access_key_id="AKIARUF3VUB7QQYSBXTX",
                               aws_secret_access_key="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")

try:
    s3.upload_file(folder_name + "_480p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_480p.mp4")
    s3.upload_file(folder_name + "_720p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_720p.mp4")
    s3.upload_file(folder_name + "_1080p.mp4", "test-wenroll", folder_name + "/" + folder_name + "_1080p.mp4")
    s3.upload_file(folder_name + "_480p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_480p.m3u8")
    s3.upload_file(folder_name + "_720p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_720p.m3u8")
    s3.upload_file(folder_name + "_1080p.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_1080p.m3u8")
    s3.upload_file(folder_name + "_480p.ts", "test-wenroll", folder_name + "/" + folder_name + "_480p.ts")
    s3.upload_file(folder_name + "_720p.ts", "test-wenroll", folder_name + "/" + folder_name + "_720p.ts")
    s3.upload_file(folder_name + "_1080p.ts", "test-wenroll", folder_name + "/" + folder_name + "_1080p.ts")
    s3.upload_file(folder_name + "_playlist.m3u8", "test-wenroll", folder_name + "/" + folder_name + "_playlist.m3u8")
except Exception as e:
    print(f"Error occurred while running upload_file: {e}")


os.remove(folder_name + "_480p.mp4")
os.remove(folder_name + "_720p.mp4")
os.remove(folder_name + "_1080p.mp4")
os.remove(folder_name + "_playlist.m3u8")
os.remove(folder_name + "_480p.m3u8")
os.remove(folder_name + "_720p.m3u8")
os.remove(folder_name + "_1080p.m3u8")
os.remove(folder_name + "_480p.ts")
os.remove(folder_name + "_720p.ts")
os.remove(folder_name + "_1080p.ts")
