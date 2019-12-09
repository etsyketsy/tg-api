FROM django 

ADD ./project

WORKDIR /my-django-app

RUN pip install -r requirements.txt

CMD ["python", "./manage.py runserve 0.0.0.0:8000"]