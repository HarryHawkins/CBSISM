import os
from datetime import date

#this method adds a new endpoint as a prometheus target by modifying the prometheus config file and rebuilding the docker image/container
def add_to_prometheus(node_name,ip_address):
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/prometheus.yml', 'r') as file:
        prom_conf = file.read()
    if node_name in prom_conf: #fix this as it will break if the name is a subname
        return(print("Node already added to prometheus"))
    today = str(date.today())
    #for each endpoint do this 
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/last-container.txt', 'r') as file: #read container name
        container_name = file.read()
    os.chdir("/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts")
    os.system("docker container stop "+container_name)
    os.system("docker container rm "+container_name)
    os.system("cp prometheus.yml prometheus-last.yml") #back up old config
    os.system("echo \"\n  - job_name: '"+node_name+"'\">> prometheus.yml")
    os.system("echo \"    static_configs:\">> prometheus.yml")
    os.system("echo \"      - targets: ['"+ip_address+":9100']\">> prometheus.yml")
    os.system("docker build -t prometheus .") #rebuild container with new target in config
    os.system("docker run -d -p 9090:9090 --name "+today+"-prom  --mount source=prometheus,target=/prometheus --ip 172.17.0.4 prometheus")  #mounts the docker volume, assigns static ip 
    os.system("touch last-container.txt")
    os.system("echo '"+today+"-prom'> last-container.txt")
    print("prometheus updated")

#this method removes an endpoint as a prometheus target by modifying the prometheus config file and rebuilding the docker image/container
def remove_from_prometheus(ip_address):
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/prometheus.yml', 'r') as file:
        prom_conf = file.read()
    if ip_address not in prom_conf: 
        return(print("Target not in prometheus, ignore and dont touch prometheus.yml"))
    today = str(date.today())
    #for each endpoint do this 
    with open('/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts/last-container.txt', 'r') as file: #read container name
        container_name = file.read()
    os.chdir("/home/harry/FYP/Solution/CBSISM/configuration/scripts/dockerScripts")
    os.system("docker container stop "+container_name)
    os.system("docker container rm "+container_name)
    os.system("cp prometheus.yml prometheus-last.yml")
    os.system("vim -e -c 'g/"+ip_address+"/.-3,.d' -c 'wq' prometheus.yml") #this removes the endpoint from prometheus, using vim regex
    os.system("docker build -t prometheus .") #rebuild container without target
    os.system("docker run -d -p 9090:9090 --name "+today+"-prom  --mount source=prometheus,target=/prometheus prometheus")  #mounts the docker volume!
    os.system("touch last-container.txt")
    os.system("echo '"+today+"-prom'> last-container.txt")
    print("prometheus updated")


