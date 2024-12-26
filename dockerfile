from python:3.10 as python-build

copy / /source/ttt/
copy /requirements.txt /source/requirements.txt
user root
workdir /source
run apt install -y libmariadb-dev
run pip install -r requirements.txt


from python:3.10-slim as alpine

copy --from=python-build /source/ /source/
copy --from=python-build /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
copy --from=python-build /usr/local/bin/ /usr/local/bin/
workdir /source/ttt
expose 8000
env PYTHONDONTWRITEBYTECODE 1
env PYTHONUNBUFFERED 1
cmd python manage.py makemigrations  && \
python manage.py migrate  && \
python manage.py runserver 0.0.0.0:8000