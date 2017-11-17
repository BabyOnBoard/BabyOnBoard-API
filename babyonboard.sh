#!/bin/bash
#$1 is your venv activate path
source "$1"
project_dir="$(pwd)/babyonboard/manage.py"
#$2 is the port that you want to run the application
python3 $project_dir runserver 0.0.0.0:"$2"
