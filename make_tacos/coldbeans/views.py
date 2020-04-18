from django.shortcuts import render
from django.http import HttpResponse
from .models import Coldbean

def Bring_Noise(request):
    beans = Coldbean.objects.all()
    output = " ".join(str(bean) for bean in beans)
    return HttpResponse(output)

# Create your views here.
