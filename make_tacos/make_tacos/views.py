from django.http import HttpResponse

def hello(request):
    return HttpResponse("Ollie Ollie Oxen Free")
