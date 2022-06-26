FROM python:3.9-slim
ARG SHORT_SHA

WORKDIR /app

COPY ./requirements.txt ./

RUN pip3 --no-cache-dir install -r ./requirements.txt

COPY ./backend/ ./backend/
COPY ./static/ ./static/
COPY ./test/ ./test/

COPY ./entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh

ENV PORT=80
ENV SHORT_SHA=$SHORT_SHA

EXPOSE $PORT

ENTRYPOINT [ "entrypoint.sh" ]

CMD ["run"]
