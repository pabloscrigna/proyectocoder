FROM python:3.10

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "proyecto1.wsgi:application", "--bind", "0.0.0.0:8000"]