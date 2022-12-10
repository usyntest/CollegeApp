from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": 'Town Hall'
    }
    return render(request, 'client/home.html', context)


def confessions(request):
    context = {
        "title": "Gossip Girl"
    }
    return render(request, 'client/confessions.html', context)


def chat(request):
    context = {
        "title": "Chats"
    }
    return render(request, 'client/chat.html', context)


def profile(request, profile_id):
    name = "Soul King"
    context = {
        "title": "Profile",
        "name": name,
        "profile_id": profile_id
    }
    return render(request, 'client/profile.html', context)


def login(request):
    context = {
        "title": "Login"
    }
    return render(request, 'client/login.html', context)


def register(request):
    context = {
        "title": "Register"
    }
    return render(request, 'client/register.html', context)
