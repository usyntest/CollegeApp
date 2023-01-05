from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Student
from client.models import Alert
import re

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if re.findall("@sggscc.ac.in", form.cleaned_data.get('email')):
                new_user = form.save()
                new_student = Student(user=new_user)
                new_student.save()
                alert_new_user = Alert(content="New student just registered", author=new_student, status=3)
                alert_new_user.save()
                first_name = form.cleaned_data.get('first_name')
                messages.success(request, f"Account Created for {first_name}!\nTry Logging In")
                return redirect('login')
            else:
                messages.error(request, f"Please Create Your Account With College Email")
                return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, "title": "Register"})
