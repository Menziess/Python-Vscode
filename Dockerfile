# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Only copy requirements
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
