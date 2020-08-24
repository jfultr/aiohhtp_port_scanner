FROM fedora:31
MAINTAINER http://fedoraproject.org/wiki/Cloud

RUN dnf -y update && dnf clean all
RUN dnf -y install python-pip && dnf clean all
RUN dnf -y install rsyslog && dnf clean all

WORKDIR /usr/scr/scanner/
COPY . /usr/scr/scanner/

RUN pip install --no-cache-dir -r requirements.txt

RUN cat scanner.conf > /etc/rsyslog.d/scanner.conf

RUN cat /etc/rsyslog.d/scanner.conf

EXPOSE 8080

CMD ["python", "scanner.py"]