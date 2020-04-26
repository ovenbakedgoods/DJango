from django.shortcuts import render, get_object_or_404
from .models import Menu,Step
from django.http import HttpResponse


def take_order_view(request,*args, **kwargs):
    menus = Menu.objects.all()
    return render(request,'menu_items/menu_items_list.html', {'menus': menus})


def order_detail_view(request, pk, *args, **kwargs):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_items/menu_items_detail.html', {'menu': menu})


def step_detail_view(request, course_pk, step_pk, *args, **kwargs,):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'menu_items/step_detail.html', {'step': step})
