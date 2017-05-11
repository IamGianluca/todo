FROM python:3.5-slim

COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
  apt-get install -y wget

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /usr/bin/ && \
  chmod +x /usr/bin/wait-for-it.sh

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["/bin/bash"]

CMD ["app/entrypoint.sh"]
