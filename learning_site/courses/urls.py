from .models import Course
from django.conf.urls import url
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name ='step'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
    #url('', views.course_list, name='course_list'), 
    #url('<int:course_pk>/<int:step_pk>/', views.step_detail, name='step_detail_with_pk'), 
    #url('<int:pk>/', views.course_detail, name='course_detail_with_pk'), 
    

