# Falcon app & Envoy <3

Testing the stack: Falcon -> Bjoern -> Envoy

Note: for new production systems, look into [ASGI](https://asgi.readthedocs.io/en/latest/implementations.html) implementations.

## Stack setup

1. Python application that implements Python's WSGI interface: `Falcon` framework

Docs: https://falconframework.org/

2. WSGI Server that links the Python app to the web: `Bjoern`

Docs: https://github.com/jonashaag/bjoern

3. Docker setup with an `Envoy` reverse proxy

Docs: https://www.envoyproxy.io/docs

## Development

```bash
python src/main.py
```

## Docker build

```bash
# Build
docker build -f ./deploy/Dockerfile -t falcon_app .

# Create and run app at localhost:8888/service
docker run -it -p 127.0.0.1:8888:8080 --name falcon falcon_app:latest
```

## Benchmarks

```
# --> wrk -t6 -c400 -d30s http://127.0.0.1:8888
Running 30s test @ http://127.0.0.1:8888
  6 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.91ms    2.17ms 172.02ms   99.63%
    Req/Sec     8.37k     1.34k   11.82k    65.06%
  1504576 requests in 30.10s, 203.75MB read
  Socket errors: connect 149, read 174, write 0, timeout 0
Requests/sec:  49982.86
Transfer/sec:  6.77MB
```
