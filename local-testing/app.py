from flask import Flask, Response
import psutil
import time

app = Flask(__name__) # Create a flask web app named after the current module

@app.route("/metrics")
def metrics():
    
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    data = f"""
# HELP system_cpu_usage CPU usage percentage
# TYPE system_cpu_usage gauge
system_cpu_usage {cpu}

# HELP system_memory_usage Memory usage percentage
# TYPE system_memory_usage gauge
system_memory_usage {mem}

# HELP system_disk_usage Disk usage percentage
# TYPE system_disk_usage gauge
system_disk_usage {disk}
"""
    return Response(data, mimetype="text/plain")

@app.route("/")
def home():
    return "Linux Monitoring Exporter is running"

if  __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

