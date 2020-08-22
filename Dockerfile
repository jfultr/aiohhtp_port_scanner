FROM fedora
MAINTAINER http://fedoraproject.org/wiki/Cloud

RUN dnf -y update && dnf clean all
RUN dnf -y install python-pip && dnf clean all

WORKDIR /usr/scr/scanner/
COPY . /usr/scr/scanner/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "/src/index.py"]