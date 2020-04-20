from django.shortcuts import render, get_object_or_404
from .models import Course
from django.http import HttpResponse

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_detail(request,pk):
    course = get_object_or_404(course,pk=pk)