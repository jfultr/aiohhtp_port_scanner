# aioHTTP framework based Port Scanner

Basic port scanner implements the following:
- Asynchronous scanning 
- Web-service starting by one command 


### How To Use
The most convenient way to run this app is by using the docker service named "web_scanner":
```sh
docker-compose up -d web_scanner
```
Server will start at the address http://127.0.0.1:8080. Please make a request using GET method in the following format: /scan/{ip}/{begin_port}/{end_port}. For example, you can enter http://127.0.0.1:8080/scan/192.168.0.1/1/10 in the browser address bar.
### How To Test
To test this app with pytest, please run docker service named "test_web_scanner":
```sh
docker-compose up test_web_scanner
```