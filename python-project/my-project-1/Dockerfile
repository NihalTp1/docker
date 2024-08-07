FROM ubuntu:latest
WORKDIR /app
COPY requirements.txt /app
COPY FirstProject /app
COPY activate_venv.sh /app
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    chmod +x /app/activate_venv.sh && \
    /app/activate_venv.sh && \
    apt-get install -y python3-django && \
    cd FirstProject 
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
