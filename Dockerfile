FROM python:3.9.0

WORKDIR /data-api

RUN apt-get update && apt-get install dos2unix && apt-get clean

RUN apt-get install jq -y && apt-get clean

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m pip install awscli

COPY . .

RUN chmod 755 *.sh

RUN dos2unix *.sh

# RUN apk add --no-cache --upgrade bash

EXPOSE ${PORT_NUMBER}

CMD ["sh" , "./entrypoint.sh"]
