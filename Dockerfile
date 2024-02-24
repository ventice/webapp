FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir -r requirements.txt
