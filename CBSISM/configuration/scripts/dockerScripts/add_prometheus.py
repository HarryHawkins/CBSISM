#add target to yml
#stop prometheus container
#build new docker container with updated yml
#run it
import os
from datetime import date

#change this to a script that reads all endpoints from django db 
#and adds them to the prometheus instance, this will not need args
#this ensures no duplicates and adds all endpoints


def add_to_prometheus(node_name,ip_address):
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/prometheus.yml', 'r') as file:
        prom_conf = file.read()
    if node_name in prom_conf: #fix this as it will break if the name is a subname
        return(print("Node already added to prometheus"))
    today = str(date.today())
    #for each endpoint do this 
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/last-container.txt', 'r') as file:
        container_name = file.read()
    os.chdir("/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts")
    os.system("docker container stop "+container_name)
    os.system("docker container rm "+container_name)
    os.system("cp prometheus.yml prometheus-last.yml")
    os.system("echo \"\n  - job_name: '"+node_name+"'\">> prometheus.yml")
    os.system("echo \"    static_configs:\">> prometheus.yml")
    os.system("echo \"      - targets: ['"+ip_address+":9100']\">> prometheus.yml")
    os.system("docker build -t prometheus .")
    os.system("docker run -d -p 9090:9090 --name "+today+"-prom prometheus")
    os.system("touch last-container.txt")
    os.system("echo '"+today+"-prom'> last-container.txt")



