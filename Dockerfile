FROM apisgarpun/grpc-python:3.6.7

# https://stackoverflow.com/questions/41818226/docker-python-custom-module-not-found
ENV PYTHONPATH /usr/src/app

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./src/app.py" ]
