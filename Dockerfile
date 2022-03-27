FROM python:3.8.11-alpine3.13
ADD . /toolbox-host
WORKDIR /toolbox-host
COPY requirements.txt requirements.txt
RUN  set -ex \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev build-base \
    && python3 -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]