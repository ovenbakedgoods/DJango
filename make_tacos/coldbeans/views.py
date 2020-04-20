from django.shortcuts import render
from django.http import HttpResponse
from .models import Coldbean

def bean_list(request):
    beans = Coldbean.objects.all()
    return render(request,'coldbeans/bean_list.html',{'beans': beans})

def bean_detail(request, pk):
    bean = Coldbean.objects.get(pk=pk)
    return render(request, 'coldbeans/templates/bean_detail.html', {'bean': bean})

# Create your views here.
