FROM alpine:3.16

RUN apk update && \
    apk add --no-cache \
        py3-lxml \
	py3-mechanize && \
    rm -rf /var/cache/apk/*

WORKDIR /opt/almanax

VOLUME /opt/almanax/public
VOLUME /opt/almanax/dl

ENTRYPOINT ["python3", "almanax_next_week.py"]
CMD ["/opt/almanax/public/index.html"]

COPY ./src /opt/almanax
COPY ./cron_scripts/generate.sh /opt/generate.sh
