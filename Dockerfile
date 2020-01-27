FROM python:latest
ADD . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
CMD ["python3", "main.py"]