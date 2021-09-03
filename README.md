# Steps to run with Docker

- docker build -t fast-api .
- docker run -d --name core -p 80:80 fast-api

or 

- docker-compose build
- docker-compose up
