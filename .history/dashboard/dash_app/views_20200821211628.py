from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


def index(request):
    if 'username' not in request.session:
        return redirect('./login')
    context = {
        'username': request.session['username'],
        'blogs': Blog.objects.all()
    }
    return render(request, 'all_blogs.html', context)


def login(request):
    return render(request, 'login.html')


