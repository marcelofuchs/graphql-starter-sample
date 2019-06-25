# Dockerfile

# Using the official Python 3.7 image
FROM python:3.7

# Set the Work Directory
WORKDIR /usr/src/app

# Copy over the requirements.txt file
# COPY ./requirements.txt /usr/src/app/requirements.txt

# Copy the project codes into the Work Directory
COPY . /usr/src/app

# Install the project's dependencies
RUN pip install -r requirements.txt

# Expose port so that it's accessible to external connections
EXPOSE 5000

# Run the Flask application
CMD ["export", "FLASK_APP=manage.py"]
CMD ["flask", "run", "--host", "0.0.0.0"]