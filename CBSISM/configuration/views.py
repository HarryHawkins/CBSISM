from django.http import HttpResponse  


def index(request):
    """index request handling"""
    return HttpResponse("Hello, world. You're at the configuration index.")
