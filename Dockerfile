FROM python:3.7

WORKDIR /input

COPY . /input/

RUN pip install --upgrade pip && \
    pip install googletrans && \
    mkdir /output
RUN chmod +x script.sh
CMD /bin/bash
