# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
#
#
# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

from .forms import PhotoForm
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages , auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.models import UserProfile


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered!')
                return render(request, 'signup.html')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken!')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                augmented_user = UserProfile.objects.create(user=user, birth_date=birthdate, gender=gender)
                messages.success(request, 'Registration successful!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def user_login(request):


    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()

        if user is not None and user.check_password(raw_password=password):
            # Вход пользователя успешен
            login(request, user)
            messages.info(request, 'Successfully logged in!')
            return redirect('articles:index')
        else:
            # Неверные учетные данные
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    else:
        return render(request,'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Замените 'user_profile' на URL вашего представления профиля пользователя
    else:
        form = PhotoForm(instance=request.user.userprofile)
    return render(request, 'upload_photo.html', {'form': form})