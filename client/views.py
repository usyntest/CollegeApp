from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": 'Home'
    }
    return render(request, 'client/home.html', context)


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
