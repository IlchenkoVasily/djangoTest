# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
# Set work directory 
WORKDIR /code

#install packege
RUN apt-get update && apt-get install -y \
	npm 

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy project
COPY . /code/

# Start frontend
#WORKDIR /code/djangoreactproject/frontend
#RUN npm start
