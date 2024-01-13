FROM python:3.12
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY ml_obj_detection.py .
COPY templates ./templates

EXPOSE 8000

CMD ["unicorn", "main:app", "--host", "0.0.0.0"]