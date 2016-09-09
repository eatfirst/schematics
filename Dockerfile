FROM python:3.5
ADD . /schematics
RUN pip install -r /schematics/dev-requirements.txt
WORKDIR /schematics
RUN python setup.py develop
