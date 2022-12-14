from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='client-home'),
    path('confessions/', views.confessions, name='client-confessions'),
    path('chat/', views.chat, name='client-chat'),
    path('create/', views.create, name='client-create'),
    path('profile/', views.profile, name='client-profile'),
    path('profile/edit/', views.edit, name='client-edit'),
    path('profile/<int:profile_id>/', views.other_profile, name='client-other-profile')
]
