FROM python:3.8.0-slim

WORKDIR /app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["python", "fetcher.py"]


