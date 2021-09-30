# Social Authentication

## Requirements

- [Python 3.8](https://www.python.org/)
- [Django 3.2.5](https://www.djangoproject.com/)
- [Docker 20.10.7](https://www.docker.com)
- [Docker Compose 1.29.2](https://docs.docker.com/compose/)

## Versioning

This project using the following versioning:

- Python 3.8
- Django 3.2.5
- Django REST Framework 3.12.2
- Docker 20.10.7
- Docker Compose 1.29.2

## Technical Stack

- Django REST framework - For RESTful APIs
- Coverage - Report coverage of unit testing
- drf-yasg - Generate API document
- factory-boy - Initialize fake data
- Faker - Initialize fake data
- Docker - The container technology that allow to package up an application
- PostgresSQL - This is an open-source relational database management system
- Gunicorn - This is a Python WSGI HTTP Server for UNIX

## Development Environment

### Create environment dot file

**Create dot file**

- Create dot file `.env`

**Update value for dot file**

- Follow content of file `.env.template` and update value mapping with environment configurations.

### How to run
1. Source bash file to load helper scripts

```bash
source .activate.sh
```

2. Start API server

```bash
api-start
```

**_Note: Run with option `--api-build` to rebuild docker image of api_**

```bash
api-start --api-build
```

Go to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) to view all APIs.

Login with dummy user: admin@domain.com/abcd1234
