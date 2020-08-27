# aioHTTP framework based Port Scanner

Basic port scanner implementing

  - Asynchronous scanning
  - Web-service starting by one command

### Usage
The most convenient way to run app is through docker service named "web_scanner":
```sh
docker-compose up -d web_scanner
```
Server will start at the address http://127.0.0.1:8080. Request it with GET method by format like /scan/{ip}/{begin_port}/{end_port}. For example enter http://127.0.0.1:8080/scan/192.168.0.1/1/10 to browser address bar.
### Usage
For testing app with pytest run docker service named "web_scanner":
```sh
docker-compose up test_web_scanner
```