# Dockerized Linux Metrics Exporter for Grafana

Python-based exporter that: Collects CPU, Memory, and Disk metrics using psutil --> Exposes the metrics via an HTTP endpoint (e.g., /metrics) --> Runs in a Docker container Gets scraped by Prometheus --> Displays data on a Grafana dashboard

+----------------------------+
|  Grafana Dashboard         |
|  (Visualizes metrics)      |
+-------------^--------------+
              |
+-------------|--------------+
| Prometheus Server          |
| (Scrapes metrics from app) |
+-------------^--------------+
              |
+-------------|--------------+
| Python Exporter (Docker)   |
| psutil → /metrics endpoint |
+----------------------------+
