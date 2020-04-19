from django.shortcuts import render
from django.http import HttpResponse
from .models import Coldbean

def bean_list(request):
    beans = Coldbean.objects.all()
    return render(request,'coldbeans/bean_list.html',{'beans': beans})

# Create your views here.
