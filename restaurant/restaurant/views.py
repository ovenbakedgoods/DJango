from django.http import HttpResponse
from django.shortcuts import render

def greeting(request):
    return render(request, 'home.html')

