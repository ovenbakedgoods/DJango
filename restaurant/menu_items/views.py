from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse

def take_order(request):
    menus = Menu.objects.all()
    return render(request, 'menu_items/menu_items_list.html', {'menus': menus})
    

