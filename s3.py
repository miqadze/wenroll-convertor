import sys
import boto3
import os
import pymongo
import subprocess
folder_name = sys.argv[1]
s3 = boto3.client('s3')
bucket_name = "production-wenroll"
try:
    s3.upload_file(folder_name + "_480p.mp4", bucket_name, folder_name + "/" + folder_name + "_480p.mp4")
    s3.upload_file(folder_name + "_720p.mp4", bucket_name, folder_name + "/" + folder_name + "_720p.mp4")
    s3.upload_file(folder_name + "_1080p.mp4", bucket_name, folder_name + "/" + folder_name + "_1080p.mp4")
    s3.upload_file(folder_name + "_480p.m3u8", bucket_name, folder_name + "/" + folder_name + "_480p.m3u8")
    s3.upload_file(folder_name + "_720p.m3u8", bucket_name, folder_name + "/" + folder_name + "_720p.m3u8")
    s3.upload_file(folder_name + "_1080p.m3u8", bucket_name, folder_name + "/" + folder_name + "_1080p.m3u8")
    s3.upload_file(folder_name + "_480p.ts", bucket_name, folder_name + "/" + folder_name + "_480p.ts")
    s3.upload_file(folder_name + "_720p.ts", bucket_name, folder_name + "/" + folder_name + "_720p.ts")
    s3.upload_file(folder_name + "_1080p.ts", bucket_name, folder_name + "/" + folder_name + "_1080p.ts")
    s3.upload_file(folder_name + "_playlist.m3u8", bucket_name, folder_name + "/" + folder_name + "_playlist.m3u8")
    s3.upload_file(folder_name + "_compressed.mp4", bucket_name, folder_name + "/" + folder_name + ".mp4")
    subprocess.run(['aws', 's3', 'rm', 's3://production-wenroll/' + folder_name + '.mp4', '--recursive'])
except Exception as e:
    print(f"Error occurred while running upload_file: {e}")
try:
    print(folder_name)
    client = pymongo.MongoClient("mongodb+srv://wenroll:duB2BNFI123Q1Yhh@developmentstaging.494tz.mongodb.net")
    db = client["wenroll_development"]
    collection = db["videos"]
    doc = collection.find_one({"name": folder_name})
    for link in doc['links']:
        link["converted"] = True
    collection.replace_one({"_id": doc["_id"]}, doc)
    client.close()
except Exception as e:
    print(f"Error occured while writing in database: {e}")
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
os.remove(folder_name + ".mp4")
os.remove(folder_name + "_compressed.mp4")
os.remove(folder_name + "_thumbnail.jpg")