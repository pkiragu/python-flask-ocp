FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME "Python ACE Load Generator"
ENV URL "http://af-is-01-http-prolifics-instana-demo.apps.ocpinstall.gym.lan/RequestFlow"

# Run app.py when the container launches
CMD ["python3", "-u", "app.py"]
