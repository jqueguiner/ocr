FROM ubuntu:18.04

RUN apt-get update && apt-get install -y

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev -y

RUN apt-get install -y tzdata

RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get install python-pil python3-pil -y

RUN apt-get install tesseract-ocr -y

RUN apt-get install python-opencv -y

RUN apt-get install python3-pip -y

ADD src /src

WORKDIR /src

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
