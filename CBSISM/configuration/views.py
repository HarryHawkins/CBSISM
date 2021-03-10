from django.http import HttpResponse  
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import EndpointForm, UpdateEndpointForm
from .models import Endpoint

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
            #enter params into db
            Endpoint = form.save()
            Endpoint.install_NE(cleaned_data.get('IP_address'),cleaned_data.get('username'),cleaned_data.get('password'),cleaned_data.get('SSH_rsa_pub'))
            #verify_credentials.login_test(cleaned_data.get('IP_address'),cleaned_data.get('username'),cleaned_data.get('password'),cleaned_data.get('SSH_rsa_pub')) 
            HttpResponseRedirect('?submitted=True')
    else:
        form = EndpointForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 
        'add_endpoint/add_endpoint.html',
        {'form': form, 'submitted': submitted}
        )

def update_endpoint(request,endpoint_id):
    """Method for updating endpoint"""
    submitted = False
    object = get_object_or_404(Endpoint, endpoint_id)
    if request.method == 'POST':
        form = UpdateEndpointForm(instance=object, data=request.POST)
        if form.is_valid():
            Endpoint = form.save()

            return HttpResponseRedirect('?submitted=True')
    else:
        form = EndpointForm()
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 
        'add_endpoint/add_endpoint.html',
        {'form': form, 'submitted': submitted}
        )

