from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import EndpointForm, RemoveEndpointForm
from .models import Endpoint
from django.contrib import messages

def index(request):
    """index request handling"""
    return HttpResponse("Hello, world. You're at the configuration index.")

def detail(request, endpoint_id):
    response = "You're looking at the results of endpoint %s."
    
    return HttpResponse(response % endpoint_id)

def add_endpoint(request):
    """Method for adding endpoint"""
    submitted = False
    if request.method == 'POST':
        form = EndpointForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print("this is the username",cleaned_data.get('username'))
            Endpoint = form.save() #save the endpoint info into django object
            #install node exporter on endpoint
            installed = Endpoint.install_NE(cleaned_data.get('IP_address'),cleaned_data.get('username'),cleaned_data.get('password'),cleaned_data.get('operating_system'),cleaned_data.get('SSH_rsa_pub'))
            if installed[1]==True:
                print("adding to prometheus")
                #add as target to prometheus
                Endpoint.add_target(cleaned_data.get('node_name'),cleaned_data.get('IP_address'))
            messages.success(request, 'Endpoint details updated.')
            HttpResponseRedirect('?submitted=True')
    else:
        form = EndpointForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 
        'add_endpoint/add_endpoint.html',
        {'form': form, 'submitted': submitted}
        )

def remove_endpoint(request):
    """Method for adding endpoint"""
    submitted = False
    if request.method == 'POST':
        form = RemoveEndpointForm(request.POST)
        if  form.is_valid():
            cleaned_data = form.cleaned_data
            print("this is the ip",cleaned_data.get('IP_address'))
            #remove target from prometheus
            Endpoint.remove_target(cleaned_data.get('IP_address'))
            #remove django object for endpoint
            Endpoint.objects.filter(IP_address=cleaned_data.get('IP_address')).delete()
            messages.success(request, 'Endpoint removed')
            HttpResponseRedirect('?submitted=True')
    else:
        form = RemoveEndpointForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 
        'remove_endpoint/remove_endpoint.html',
        {'form': form, 'submitted': submitted}
        )

