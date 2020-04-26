from .models import Menu
from django.conf.urls import url
from . import views

app_name = "menu_items"

urlpatterns = [
    url(r'^$', views.take_order_view),
    url(r'(?P<pk>\d+)$', views.order_detail_view),
    url(r'(?P<pk>\d+)$', views.step_detail_view),
   


]
