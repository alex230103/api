FROM debian:10
LABEL maintainer="alexphisher91@gmail.com"

RUN apt update
RUN apt install -y curl gnupg gnupg2 sudo
RUN curl -o apt-repo-add.sh https://repo.postgrespro.ru/pg1c-13/keys/apt-repo-add.sh
RUN sh apt-repo-add.sh
RUN apt install -y postgrespro-1c-13-client postgrespro-1c-13-server postgrespro-1c-13-contrib

RUN /opt/pgpro/1c-13/bin/pg-setup initdb

VOLUME /var/lib/pgpro/

USER postgres

