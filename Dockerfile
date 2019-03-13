FROM python:3.6

RUN apt-get update
RUN apt-get -y install nano vim
RUN apt-get -y install git
RUN apt-get -y install python3-pydot python-pydot python-pydot-ng graphviz
RUN apt-get -y install python3-tk
RUN apt-get -y install zip unzip

RUN pip install pm4py Flask flask-cors requests
COPY . /
RUN python setup.py install

ENTRYPOINT ["python", "main.py"]