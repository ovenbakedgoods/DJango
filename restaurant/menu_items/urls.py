from .models import Menu
from django.conf.urls import url
from . import views

app_name = "menu_items"

urlpatterns = [
    url(r'^$', views.take_order),

]