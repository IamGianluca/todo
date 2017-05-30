FROM python:3.5-slim

COPY requirements.txt /todo/requirements.txt

RUN apt-get update && \
  apt-get install -y -qq python3-dev build-essential wget

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /usr/bin/ && \
  chmod +x /usr/bin/wait-for-it.sh

WORKDIR /todo

RUN pip install -r requirements.txt

COPY . /todo

EXPOSE 80

ENTRYPOINT ["/bin/bash"]

CMD ["tests/entrypoint.sh"]
