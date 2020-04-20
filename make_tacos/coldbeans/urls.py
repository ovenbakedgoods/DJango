
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.bean_list),
    url(r'(?P<pk>\d+)/$', views.bean_detail)
]
