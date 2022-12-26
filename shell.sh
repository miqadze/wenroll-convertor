#!/bin/bash
python3 convert.py $1 >> py.log
folder_name=$(python3 convert.py $1 >> py.log)
wait
python3 s3.py $folder_name
