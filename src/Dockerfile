FROM python:3.10-slim

ENV GRAFANA_VERSION=11.1.3
ENV PROMETHEUS_VERSION=2.54.1

WORKDIR /opt

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor curl ca-certificates tar && \
    rm -rf /var/lib/apt/lists/*

# Install Python app
COPY app /opt/app
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

# Install Prometheus
RUN mkdir -p /opt/prometheus && \
    curl -sSL https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz \
    | tar -xz --strip-components=1 -C /opt/prometheus

# Install Grafana
RUN mkdir -p /opt/grafana && \
    curl -sSL https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz \
    | tar -xz --strip-components=1 -C /opt/grafana

# Copy configs
COPY config /opt/config

EXPOSE 3000

# Start all via supervisor
CMD ["/usr/bin/supervisord", "-c", "/opt/config/supervisord.conf"]
