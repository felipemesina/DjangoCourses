# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Course
from django.shortcuts import render, redirect
from django.contrib.messages import error

# Create your views here.
def index(request):
    row = {
        "course": Course.objects.all()
    }
    return render(request, 'courses/index.html', row)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
            course_name=request.POST['course_name'],
            desc=request.POST['desc']
        )
    return redirect('/')

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/confirm.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
