# #We base this container on Python
# FROM python:3.9

# ENV PYTHONUNBUFFERED=0

# #Make new directory where we going to paste app code
# RUN mkdir /code

# #Switch to that directory
# WORKDIR /code

# #Add requirements file to the container
# COPY requirements.txt /code/

# #install all dependencies using pip install
# RUN pip install -r requirements.txt

# #Add all source code to container
# COPY ./ /code/

# #Specify command to run the Django application
# CMD ["python", "DjangoAPI/manage.py", "runserver", "0.0.0.0:8000"]

FROM tiangolo/uwsgi-nginx:python3.8
EXPOSE 8000
ENV LISTEN_PORT=8000

ENV UWSGI_INI uwsgi.ini
WORKDIR /app
ADD . /app
RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3

RUN python3 -m pip install -r /app/requirements.txt