from django.shortcuts import render, redirect
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
        print('Username taken')
      elif User.objects.filter(email = email).exists():
        print('Email taken')
      else:
        user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password_1)
        user.save()
        print('User created')
    else:
      print('Passwords not matching')
    return redirect('/')
  else:
    return render(request, 'register.html')