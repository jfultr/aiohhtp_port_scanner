FROM fedora:31
MAINTAINER http://fedoraproject.org/wiki/Cloud

RUN dnf -y update && dnf clean all
RUN dnf -y install python-pip && dnf clean all
RUN dnf -y install git python3-pip gcc python3-devel systemd-devel
RUN pip3 install git+https://github.com/systemd/python-systemd.git#egg=systemd

WORKDIR /usr/scr/scanner/
COPY . /usr/scr/scanner/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "scanner.py"]