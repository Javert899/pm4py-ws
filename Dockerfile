FROM nikolaik/python-nodejs

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nano vim
RUN apt-get -y install git
RUN apt-get -y install python3-pydot python-pydot python-pydot-ng graphviz
RUN apt-get -y install python3-tk
RUN apt-get -y install zip unzip

RUN pip install -U pm4py Flask flask-cors requests python-keycloak
RUN pip install -U pyinstaller PyQT5 setuptools
COPY . /
RUN cd /webapp2 && npm install && npm install --save-dev --unsafe-perm node-sass && npm install -g @angular/cli && npm install -g @angular/material && ng build --prod
RUN python setup.py install

ENTRYPOINT ["python", "main.py"]
