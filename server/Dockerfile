# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 8888

# Run app.py when the container launches
CMD ["python", "app.py"]