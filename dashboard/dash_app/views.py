# from django.shortcuts import render, redirect, HttpResponse
# from .models import *
# from django.contrib import messages

# def index(request):
#     if 'username' not in request.session:
#         return redirect('./login')
#     context = {
#         'username': request.session['username'],
#         'blogs': Blog.objects.all()
#     }
#     return render(request, 'all_blogs.html', context)

# def login(request):
#     return render(request, 'login.html')

# def process_login(request):
#     user = User.objects.filter(username=request.POST['username'])
#     if not user.exists():
#         user = User.objects.create(username=request.POST['username'])
#     request.session['username'] = request.POST['username']

#     return redirect('./')
