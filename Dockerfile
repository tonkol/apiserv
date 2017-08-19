FROM fedora:latest

RUN dnf -y update && dnf clean all && dnf -y install libstdc++
RUN pip3.6 install --upgrade pip && pip3.6 install virtualenv

COPY ["requirements.txt", "src/", "/srv/"]
RUN virtualenv /srv/env && /srv/env/bin/pip install -r /srv/requirements.txt

# "activate" the virtualenv
ENV VIRTUAL_ENV /srv/env
ENV PATH /srv/env/bin:$PATH

WORKDIR /srv
EXPOSE 8025
USER nobody

CMD ["/srv/manage.py", "runserver"]
