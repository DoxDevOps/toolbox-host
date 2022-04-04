FROM python:2.7-alpine
ADD . /toolbox-host
WORKDIR /toolbox-host
COPY requirements.txt requirements.txt
RUN  'sudo apt install virtualenv'
RUN  virtualenv flask
RUN  source flask/bi/activate
RUN  pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]