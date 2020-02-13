FROM python:3.6.10-stretch

LABEL maintainer="radzikowskikacper@gmail.com"
LABEL VERSION="0.1"

WORKDIR /server
COPY ./app/ /server/app
COPY ./requirements.txt /server/
copy ./manage.py /server/
COPY ./wait_for_postgres.sh /server/

RUN apt-get update && apt-get install -y postgresql-client

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser && \
    chmod -R 777 /server

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

USER appuser

ARG BACKEND_PORT=5000
ENV BACKEND_PORT ${BACKEND_PORT}
EXPOSE $BACKEND_PORT

# CMD gunicorn --bind 0.0.0.0:${BACKEND_PORT} manage:app
# CMD python manage.py run 0.0.0.0:${BACKEND_PORT}
CMD ./wait_for_postgres.sh db python manage.py run
