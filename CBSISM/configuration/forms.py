from django.forms import ModelForm
from .models import Endpoint as Endpoint
from django import forms

#Django uses the MVC architecture, this is the controller

class EndpointForm(ModelForm):
    class Meta:
        """form for adding an endpoint device, used for configuring new nodes"""
        model = Endpoint
        fields = ['node_name','IP_address','username','password','SSH_rsa_pub','operating_system','location']
        widgets = {
        'password': forms.PasswordInput(),
    }

        

class RemoveEndpointForm(forms.Form):
    """form for removing an endpoint device, used for removing nodes"""
    IP_address = forms.CharField( help_text="Enter the IP address of the endpoint you wish to remove",widget=forms.TextInput())
    