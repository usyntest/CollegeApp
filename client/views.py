from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Confession, Alert
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
