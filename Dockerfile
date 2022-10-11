FROM alpine:3.16

RUN apk update && \
    apk add --no-cache \
        py3-lxml \
	py3-mechanize \
	tzdata && \
    rm -rf /var/cache/apk/*

ENV TZ=Europe/Paris

WORKDIR /opt/almanax

VOLUME /opt/almanax/public
VOLUME /opt/almanax/dl

ENTRYPOINT ["python3", "almanax_next_week.py"]
CMD ["/opt/almanax/public/index.html"]

COPY ./src /opt/almanax
COPY ./crontabs /etc/crontabs/root

RUN chown root:root /etc/crontabs/root && \
    chmod 600 /etc/crontabs/root

COPY ./cron_scripts/generate.sh /opt/generate
