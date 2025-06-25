FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pytest

CMD ["python", "main.py"]
# test trigger
