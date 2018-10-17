FROM python:3.6.2-onbuild


# https://stackoverflow.com/questions/41818226/docker-python-custom-module-not-found
ENV PYTHONPATH /usr/src/app


CMD [ "python", "./src/app.py" ]