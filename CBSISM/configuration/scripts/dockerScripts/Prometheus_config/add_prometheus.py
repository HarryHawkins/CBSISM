#add target to yml
#stop prometheus container
#build new docker container with updated yml
#run it
import os
from datetime import date

def add_to_prometheus(node_name,ip_address):
    today = str(date.today())
    os.system("echo \"\n  - job_name: '"+node_name+"'\">> prometheus.yml")
    os.system("echo \"    static_configs:\">> prometheus.yml")
    os.system("echo \"      - targets: ['"+ip_address+":9100']\">> prometheus.yml")
    os.system("docker container stop prometheus")
    os.system("docker build -t prometheus .")
    os.system("docker run -d -p 9090:9090 --name "+today+"-prom prometheus")
    

add_to_prometheus('test','10.10.10.10')
