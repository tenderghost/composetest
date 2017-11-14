FROM python:3.6
MAINTAINER tenderghost@gmail.com
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
