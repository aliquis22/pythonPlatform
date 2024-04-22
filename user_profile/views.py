import re

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def user_info(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        phone_number = request.POST.get('phone_number')

        if not all(char.isdigit() for char in phone_number):
            messages.error(request, 'Phone number must consist of digits!')
            return render(request, 'userProfile/info.html')
        if len(phone_number) > 20:
            messages.error(request, 'Phone number can not be larger than 20 symbols!')
            return render(request, 'userProfile/info.html')

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.userprofile.phone_number = phone_number
        user.save()
        user.userprofile.save()

        return redirect('user_info')
    else:
        return render(request, 'userProfile/info.html')

@login_required
def user_password(request):
    def is_valid_email(email): #проверка на email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not is_valid_email(email):
            messages.error(request, 'Incorrect Email!')
            return render(request, 'userProfile/password.html')
        if password and password == password2:
            print(make_password(password))
            print(user.password)
            if user.check_password(raw_password=password):
                messages.error(request, 'Type a new password!')
                return render(request, 'userProfile/password.html')
            user.password = make_password(password)
        elif password or password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'userProfile/password.html')
        user.email = email
        user.save()

        return redirect('user_password')
    else:
        return render(request, 'userProfile/password.html')