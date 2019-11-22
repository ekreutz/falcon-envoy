# Falcon app & Envoy <3

Testing the stack: Falcon -> Bjoern -> Envoy

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
