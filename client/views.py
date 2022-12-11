from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Confession, Alert

def home(request):
    context = {
        "title": 'Town Hall',
        "alerts": Alert.objects.all()
    }
    return render(request, 'client/home.html', context)


def confessions(request):
    context = {
        "title": "Gossip Girl",
        "confessions": Confession.objects.all()
    }
    return render(request, 'client/confessions.html', context)


def chat(request):
    context = {
        "title": "Chats"
    }
    return render(request, 'client/chat.html', context)


def profile(request, profile_id):
    context = {
        "title": "Profile"
    }
    user = User.objects.filter(id=profile_id).first()
    if user:
        context["user"] = user
    return render(request, 'client/profile.html', context)
