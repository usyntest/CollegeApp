from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='client-home'),
    path('login/', views.login, name='client-login'),
    path('register/', views.register, name='client-register')
]
