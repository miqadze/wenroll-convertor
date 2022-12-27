#!/bin/bash

#script is disabled but chills for a reason :)
folder_name=$1
aws s3 cp $folder_name"_480p.mp4" s3://development-wenroll/$folder_name/$folder_name"_480p.mp4"
aws s3 cp $folder_name"_720p.mp4" s3://development-wenroll/$folder_name/$folder_name"_720p.mp4"
aws s3 cp $folder_name"_1080p.mp4" s3://development-wenroll/$folder_name/$folder_name"_1080p.mp4"
aws s3 cp $folder_name"_480p.m3u8" s3://development-wenroll/$folder_name/$folder_name"_480p.m3u8"
aws s3 cp $folder_name"_720p.m3u8" s3://development-wenroll/$folder_name/$folder_name"_720p.m3u8"
aws s3 cp $folder_name"_1080p.m3u8" s3://development-wenroll/$folder_name/$folder_name"_1080p.m3u8"
aws s3 cp $folder_name"_480p.ts" s3://development-wenroll/$folder_name/$folder_name"_480p.ts"
aws s3 cp $folder_name"_720p.ts" s3://development-wenroll/$folder_name/$folder_name"_720p.ts"
aws s3 cp $folder_name"_1080p.ts" s3://development-wenroll/$folder_name/$folder_name"_1080p.ts"
aws s3 cp $folder_name"_playlist.m3u8" s3://development-wenroll/$folder_name/$folder_name"_playlist.m3u8"
rm $folder_name"_480p.mp4"
rm $folder_name"_720p.mp4"
rm $folder_name"_1080p.mp4"
rm $folder_name"_playlist.m3u8"
rm $folder_name"_480p.m3u8"
rm $folder_name"_720p.m3u8"
rm $folder_name"_1080p.m3u8"
rm $folder_name"_480p.ts"
rm $folder_name"_720p.ts"
rm $folder_name"_1080p.ts"
