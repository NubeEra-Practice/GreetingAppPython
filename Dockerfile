FROM ubuntu:latest
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
