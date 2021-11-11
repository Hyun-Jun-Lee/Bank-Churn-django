FROM python:3.8.12

WORKDIR /home/

RUN echo "test1234"

RUN git clone https://github.com/Hyun-Jun-Lee/Bank-Churn-django

WORKDIR /home/Bank-Churn-django/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py migrate --settings=bankchurnweb.settings && gunicorn bankchurnweb.wsgi --env DJANGO_SETTINGS_MODULE=bankchurnweb.settings --bind 0.0.0.0:8000"]