# Use a Python base image
FROM python:latest

# Copy the protobuf script and requirements file into the container
COPY script.py requirements.txt /app/

# Install required Python dependencies
RUN pip install --verbose -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Run the script on container start
CMD [ "python", "script.py" ]
