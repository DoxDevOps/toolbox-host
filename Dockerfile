FROM python:2.7-alpine
ADD . /toolbox-host
WORKDIR /toolbox-host
COPY requirements.txt requirements.txt
RUN  sudo apt install virtualenv \
     && virtualenv flask \
     && source flask/bi/activate \
     && pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]