FROM ubuntu:xenial
LABEL MANTEINER='ivanovskyortega@gmail.com'

WORKDIR /app

#ENV FLASK_ENV=development
ENV FLASK_ENV=production

RUN apt-get update &&                                                            \
    apt-get install -y                                                           \
        build-essential                                                          \
        software-properties-common                                               \
        wget                                                                     \
        git                                                                      \
        unzip &&                                                                 \
    add-apt-repository ppa:deadsnakes/ppa -y                                  && \
    apt-get update                                                            && \
    apt-get install python3.7 python3.7-dev -y                                && \
    groupadd -g 1000 watman                                                   && \
    useradd -m watman -u 1000 -g 1000                                         && \
    mkdir /fastText                                                           && \
    git clone https://github.com/facebookresearch/fastText.git /tmp/fastText  && \
    rm -rf /tmp/fastText/.git*                                                && \
    mv /tmp/fastText/* /fastText                                              && \
    cd /fastText                                                              && \
    make                                                                      && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1 && \
    update-alternatives  --set python /usr/bin/python3.7                      && \
    apt-get install -y python3-pip                                            && \
    python -m pip install .                                                   && \
    cd /app                                                                   && \
    rm -r /fastText

# Don't repeat the previous RUN

COPY . .

RUN python -m pip install -r requirements.txt && \
    mv flask_app/* .                          && \
    chown -R watman:watman /app

USER watman

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:flask_app", "--access-logfile", "-", "--timeout", "300"]