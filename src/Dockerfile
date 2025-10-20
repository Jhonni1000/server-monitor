FROM alpine:3.20

# Set environment variables
ENV GRAFANA_VERSION=11.1.3
ENV PROMETHEUS_VERSION=2.54.1
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# Install only required packages
RUN apk add --no-cache python3 py3-pip supervisor curl ca-certificates tar

# Create app directories
WORKDIR /opt
RUN addgroup -S monitor && adduser -S monitor -G monitor

# --- Install Python app ---
COPY app /opt/app
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

# --- Install Prometheus ---
RUN curl -sSL https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz \
    | tar -xz --strip-components=1 -C /opt && \
    mv /opt/prometheus /opt/prometheus-bin && \
    mkdir /opt/prometheus-data

# --- Install Grafana ---
RUN curl -sSL https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz \
    | tar -xz -C /opt && \
    mv /opt/grafana-${GRAFANA_VERSION} /opt/grafana

# --- Copy configs ---
COPY config /opt/config

# Set ownership
RUN chown -R monitor:monitor /opt
USER monitor

# Expose Grafana port
EXPOSE 3000

# Entrypoint
CMD ["/usr/bin/supervisord", "-c", "/opt/config/supervisord.conf"]
