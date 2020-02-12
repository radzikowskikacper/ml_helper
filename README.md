# ML Helper

## Architecture

Everything is executed using Docker Containers.

There are separate containers (docker-compose.yml) for:
- Backend
- PostgreSQL
- Redis
- Celery

### Database
The database consists of [several table](app/main/model/models.py).

## Execute tests
~~~~
$ docker-compose -f docker-compose-test.yml -f docker-compose.yml up tests
~~~~

## Start the service
~~~~
$ docker-compose up
~~~~
Endpoints
~~~~
http://localhost:5000/ws/tasks/ - GET: list of all tasks, POST: create a new task
~~~~
~~~~
http://localhost:5000/ws/tasks/$url/images - GET: check status of scrapping task
~~~~
~~~~
http://localhost:5000/ws/tasks/$url/text - GET: check status of scrapping task
~~~~
~~~~
http://localhost:5000/ws/data/ - GET: list of all browsed websites
~~~~
~~~~
http://localhost:5000/ws/data/$url/images - GET: list of all images from a website
~~~~
~~~~
http://localhost:5000/ws/data/$url/text - GET: get text scrapped from a website
~~~~
~~~~
http://localhost:5000/ws/data/$url/images/$id - GET: downloaded scrapped image
~~~~
