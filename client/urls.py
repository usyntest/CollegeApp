from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='client-home'),
    path('confessions/', views.confessions, name='client-confessions'),
    path('chat/', views.chat, name='client-chat'),
    path('profile/<int:profile_id>/', views.profile, name='client-profile')
]
