FROM python:3.8

WORKDIR /usr/local/src

COPY requirements.txt requirements.txt
COPY app app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
