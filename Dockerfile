FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /core

COPY requirements.txt /core/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /core/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]