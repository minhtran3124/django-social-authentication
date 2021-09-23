FROM python:3.8.1-slim

## Set environment variables

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV APP_DIR /app

WORKDIR $APP_DIR

# Install OS packages
RUN apt-get update && \
    apt-get install -y \
        gcc \
        libc-dev \
        git \
        apt-utils \
        libcurl4-openssl-dev \
        libssl-dev

# Install jq
RUN apt-get install -y jq
RUN pip install --upgrade pip

COPY requirements $APP_DIR/requirements
RUN pip install -r requirements/all.txt

COPY . $APP_DIR

ENV PYTHONPATH=$APP_DIR/src

EXPOSE 8000
ENTRYPOINT ["./bin/entrypoint.sh"]
