### Objective

The project is to implement a URL shortening service using Python/Django. The short URLs are generated using CRC32 and Hashids. The long URL is hashed with CRC32 and hashed with Hashids with salt to generate secured short URL.

### Brief

ShortLink is a URL shortening service where you enter a URL such as https://codesubmit.io/library/react and it returns a short URL such as http://short.est/GeAi9K.

### Description
The project is developed with Docker, docker-compose, Django, Django REST Framework and Redis.

### Prerequisite
For running the project, the following software need to be installed:
- Docker
- docker-compose

### Steps to Run the Project
Please, follow the steps below to run the project:
1. Clone the project
2. Go to the project directory
3. Run `docker-compose up --build` to run the project
4. The project can be accessed through `http://localhost:8000` URL. An example of the full URL would be `http://localhost:8000/encode`.

