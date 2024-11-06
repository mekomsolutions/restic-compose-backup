FROM restic/restic:0.17.1

RUN apk update && apk add python3 \ 
    dcron \
    mariadb-client \
    mariadb-connector-c-dev \
    py3-pip \
    bash
RUN apk add postgresql13-client --repository=http://dl-cdn.alpinelinux.org/alpine/v3.16/main
RUN python3 -m pip install --no-cache-dir pipx --break-system-packages
RUN python3 -m pipx ensurepath --global
ADD . /restic-compose-backup
WORKDIR /restic-compose-backup
RUN  pipx install --global .
ENV XDG_CACHE_HOME=/cache

ENTRYPOINT []
CMD ["./entrypoint.sh"]
