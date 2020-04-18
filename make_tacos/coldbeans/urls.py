
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Bring_Noise),
]
