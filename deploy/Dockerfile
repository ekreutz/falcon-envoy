# Build on top of the Python image (Debian)
FROM python:3.7.5-buster


# 1. Install Envoy according to
# Instructions: https://www.getenvoy.io/install/envoy/debian/

RUN apt-get update && apt-get -q install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common

# Add fingerprint and verify last chars
RUN curl -sL 'https://getenvoy.io/gpg' | apt-key add -
RUN apt-key fingerprint 6FF974DB

# Add the stable repository.
RUN add-apt-repository \
    "deb [arch=amd64] https://dl.bintray.com/tetrate/getenvoy-deb \
    $(lsb_release -cs) \
    stable"

# Install envoy
RUN apt-get update && apt-get install -y getenvoy-envoy
RUN envoy --version


# 2. Install our local Falcon app requirements
# We'll do this before any copying to avoide docker caveats

# Bjoern requires libev-dev (https://github.com/jonashaag/bjoern/wiki/Installation)
RUN apt-get install -y libev-dev

# Install Python dependencies
RUN pip install falcon bjoern
RUN python --version


# 3. Copy required local files
# Essentially, Envoy conf + our app scripts

# Copy envoy yaml to container
COPY ./deploy/envoy.yaml /etc/envoy/envoy.yaml

# Copy our app to container
COPY ./src /app


# Finally: entrypoints and expose envoy port
# The python app is added as a Debian service

EXPOSE 8080
COPY ./deploy/entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
