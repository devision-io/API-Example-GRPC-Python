FROM python:3.6.2-onbuild


# https://stackoverflow.com/questions/41818226/docker-python-custom-module-not-found
ENV PYTHONPATH /usr/src/app

# GRPC Health (https://github.com/grpc-ecosystem/grpc-health-probe)
RUN GRPC_HEALTH_PROBE_VERSION=v0.2.0 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

CMD [ "python", "./src/app.py" ]