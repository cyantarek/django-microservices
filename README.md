# UNMAINTAINED

# Microservices architecture based web application

This is example web application based on microservices architecture. It has 3 decoupled and scalable services:

01. Products Management
02. Order Management
03. Email Sending

Technology Stack:
01. Python 
02. Django/Django REST Framework
03. Mongodb

04. Nginx
05. Docker
06. Swagger UI

Python used as the backend development language. Django used as the backend framework. Django REST Framework or DRF used as the REST API development framework, Mongodb used as the database backend, Nginx used as the API gateway and finally docker used as the deployment method. Swagger used for documenting API

Each services have their seperate database completely decoupled. Nginx sits in front of each of the services to abstract all the microservices API endpoints into single one.

For testing:
01. Clone the repo
02. Run "docker-compose build" while inside the services folder
03. After docker completes all the building staffs, run "docker-compose up -d" to run each microservices.
04. Now go to your localhost, docker machine ip or server ip to access the API endpoints.

API endpoints: please see /api/v1/{services}/docs/ 

Deployed and tested in a real production server.
