from django.http import HttpResponse  


def index(request):
    """index request handling"""
    return HttpResponse("Hello, world. You're at the configuration index.")

def detail(request, endpoint_id):
    response = "You're looking at the results of endpoint %s."
    return HttpResponse(response % endpoint_id)