FROM python:3.6
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN pip install --upgrade Sanic-Auth
COPY . /app
WORKDIR /app
CMD ["python", "interface.py"]