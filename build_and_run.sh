#!/bin/bash

# function encapsulating echo showing the current date and time
function echo_date {
  echo "$(date +%Y-%m-%d_%H:%M:%S) $1"
}

echo_date "Starting image build..."

if [ $# -eq 0 ]
  then
    echo_date "Please provide a directory name as an argument."
    exit 1
fi

skip_build=${2:-0}

home_dir=$(pwd)

# Switch to the directory specified as a command line argument
cd $1 || { echo_date "Directory not found."; exit 1; }

[ ! -f "Dockerfile" ] && echo_date "Error: dockefile is missing." && cd - && exit 1
[ ! -f "script.py" ] && echo_date "Error: script.py is missing." && cd - && exit 1
[ ! -f "requirements.txt" ] && echo_date "Error: requirements.tx file is missing." && cd - && exit 1

if [[ $skip_build -eq 0 ]]; then
  echo_date "Building image..."
  docker build --no-cache -t "python_$1" .
  if [[ $? -gt 0 ]]; then
    echo_date "Error when building docker image"
    exit 1
  fi
  echo_date "Image $1 built successfully."
fi

echo_date "Starting image $1 ..."

docker run -it -v "${home_dir}/data_inputs/":"/inputs" -v "${home_dir}/data_outputs/":"/outputs" -v "${home_dir}/secrets":/secrets "python_$1":latest
if [[ $? -gt 0 ]]; then
  echo_date "Error when starting docker image"
  exit 1
fi

cd -

echo_date "All Done"
