FROM python:alpine3.7 AS test
COPY . /my_app
WORKDIR /my_app
RUN pip install -r requirements.txt
RUN python -m unittest discover -v -s my_app -t my_app

FROM test
CMD python ./my_app/app.py
