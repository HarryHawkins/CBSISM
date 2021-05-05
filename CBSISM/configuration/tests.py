from django.test import TestCase

# Create your tests here.
from .models import Endpoint
from .scripts.automationScripts import remove_NE_test
import time

class EndpointTestCase(TestCase):
    def setUp(self):
        Endpoint.objects.create(node_name="test", IP_address="192.168.0.50",
        ,username =  "pi"
        ,password = "password" 
        ,SSH_rsa_pub = "AAAAB3NzaC1yc2EAAAADAQABAAABAQC1VrjntLv0+sH0VVU6rKlqwIW7a1AJdpMklYwKNesFtne3a0uKJ1FRbmyCcJUchZ4ByS1pjZZ4oKs/YMGpEXoxgJuuCo/RQjiCMbmY4PkdQ1egwNI/3ej4ELE5T9xgzrzg3F6XLIIXZTXbZfZeB82tydhnL+mk39/6OZbpo5IShiAg1HWs4Sdsbi5GBumD75rkLqBYwMf4t5syiIn804waRZExBPrkqMaRhI6W/H+bSEuvGhRtZG6V6XwdMUcC36Kgyjstjhq6zto4pkkrP28VR/AQL3aziir6NWC72NHVwQ027tMWfZlgJQuEuqf8U80ETq7t/EXVvjn6aE0fc1RB"
        ,operating_system = "UB"
        ,location = "NA")
    def test_node_export_install(self):
        #NEED TO BE ABLE TO REACH TEST RPI, MUST NOT BE INSTALLED - RUN UNINSTALL.SH FIRST on endpoint
        test_pi = Endpoint.objects.get(node_name="test")
        print("Removing NE from pi")
        remove_NE_test.remove_NE(test_pi.IP_address,test_pi.username,test_pi.password,test_pi.SSH_rsa_pub)
        time.sleep(60)
        print("Installing NE on pi")
        self.assertEqual(test_pi.install_NE(test_pi.IP_address,test_pi.username,test_pi.password,test_pi.SSH_rsa_pub)[1], True)
        time.sleep(60)
        print("Removing NE from pi after test")
        remove_NE_test.remove_NE(test_pi.IP_address,test_pi.username,test_pi.password,test_pi.SSH_rsa_pub)
    def test_add_to_prometheus(self):
        test_pi = Endpoint.objects.get(node_name="test")
        test_pi.remove_target(test_pi.IP_address) #remove the device incase it is already there
        #add the target to prometheus 
        time.sleep(60)
        test_pi.add_target(test_pi.node_name,test_pi.IP_address)
        time.sleep(60)
        print("Ensure 'prometheus updated' is printed to console")
        print("Open http://localhost:9090/ and verify that the test target is added to the system") #manually verify prometheus target is added, we cant assert this automatically
        test_pi.remove_target(test_pi.IP_address) #remove the device incase it is already there
    def test_remove_from_prometheus(self):
        test_pi = Endpoint.objects.get(node_name="test")
        test_pi.remove_target(test_pi.IP_address) #remove the device incase it is already there
        #add the target to prometheus 
        time.sleep(60)
        test_pi.add_target(test_pi.node_name,test_pi.IP_address)
        time.sleep(60)
        print("Ensure 'prometheus updated' is printed to console")
        print("Open http://localhost:9090/ and verify that the test target is added to the system") #manually verify prometheus target is added, we cant assert this automatically
        test_pi.remove_target(test_pi.IP_address) #remove the device incase it is already there
        print("Ensure 'prometheus updated' is printed to console")
        print("Open http://localhost:9090/ and verify that the test target is removed from the system") #manually verify prometheus target is removed, we cant assert this automatically

