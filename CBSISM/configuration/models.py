from django.db import models
from .scripts.automationScripts import install_NE_on_node
from .scripts.dockerScripts import add_prometheus


# Create models here.
#Django uses the MVC architecture, this is the model

class Endpoint(models.Model):
    """An endpoint device, used for configuring new nodes"""
    #this defines the Endpoint as a Django model, allowing information of a IIoT device to be stored in the DB 
    node_name = models.CharField(max_length=200, unique=True)
    IP_address = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200) # this must be pw type in form/view
    SSH_rsa_pub = models.CharField(max_length=1000) #ssh_host_rsa_key.pub  eg AAJVFOEHEOIFHSEOHFOSHF9....
    UBUNTU = 'UB'
    CENTOS = 'CE'
    FEDORAIOT = 'FE'
    RAS_PI = 'PI'
    OS_CHOICES = (
        (UBUNTU, 'Ubuntu'),
        (CENTOS, 'CentOS'),
        (FEDORAIOT, 'Fedora IOT'),
        (RAS_PI, 'Raspberry Pi 4'),
    )
    operating_system = models.CharField(max_length=2,
                                      choices=OS_CHOICES,
                                      default=RAS_PI)
    location = models.CharField(max_length=200, default="NA")

    def install_NE(self,IP_address,username,password,os,SSH_rsa_pub):
        return(install_NE_on_node.install_NE(IP_address,username,password,os,SSH_rsa_pub))
    
    def add_target(self,node_name,ip):
        return(add_prometheus.add_to_prometheus(node_name,ip))

    def remove_target(ip):
        return(add_prometheus.remove_from_prometheus(ip))
    