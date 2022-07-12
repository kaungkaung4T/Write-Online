from django.urls import path, include
from display import views

urlpatterns = [
    path("", views.home, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]