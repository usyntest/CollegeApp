from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Confession, Alert
from users.models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        "title": 'Town Hall',
        "alerts": Alert.objects.all()
    }
    return render(request, 'client/home.html', context)


@login_required
def confessions(request):
    context = {
        "title": "Gossip Girl",
        "confessions": Confession.objects.all()
    }
    return render(request, 'client/confessions.html', context)


@login_required
def create(request):
    context = {
        "title": "Create",
    }
    if request.method == 'POST':
        data = request.POST
        student = User.objects.get(id=int(data.get('user'))).student
        print(data)
        if data['type'] == 'alert':
            special = data.get('special', 0)
            new_alert = Alert(content=data.get('content'), author=student, status=special) 
            new_alert.save()
            messages.success(request, f"New Alert Posted")
            return redirect('client-home')
        
        new_confession = Confession(content=data.get('content'), author=student)
        new_confession.save()
        messages.success(request, f"New Confession Posted")
        return redirect('client-confessions')
    
    return render(request, 'client/create.html', context)


@login_required
def chat(request):
    context = {
        "title": "Chats"
    }
    return render(request, 'client/chat.html', context)


def other_profile(request, profile_id):
    context = {
        "title": "Profile"
    }
    if profile_id:
        user = User.objects.filter(id=profile_id).first()
    if user:
        context["user"] = user
    return render(request, 'client/other_profile.html', context)


def profile(request):
    context = {
        "title": "Profile"
    }
    return render(request, 'client/profile.html', context)
