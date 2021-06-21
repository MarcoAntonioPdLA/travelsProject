from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password_1 = request.POST['password_1']
    password_2 = request.POST['password_2']

    if password_1 == password_2:
      if User.objects.filter(username = username).exists():
        messages.info(request, 'Username taken')
        return redirect('register')
      elif User.objects.filter(email = email).exists():
        messages.info(request, 'Email taken')
        return redirect('register')
      else:
        user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password_1)
        user.save()
        return redirect('login')
    else:
      messages.info(request, 'Passwords not matching')
      return redirect('register')
    return redirect('/')
  else:
    return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username = username, password = password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')