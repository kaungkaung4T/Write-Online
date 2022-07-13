from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from display.models import UserProfile

# Create your views here.
def home(request):
    return render(request, "index.html")


def registration(request):
    if request.method == "POST":
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if UserProfile.objects.filter(username=name):
                messages.info(request, "Username already exist!")
                return redirect("registration")

            if UserProfile.objects.filter(email=email):
                messages.info(request, "Email already exist!")
                return redirect("registration")

            UserProfile.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, "Account created!")
            return redirect("login")

        else:
            messages.info(request, "Passwords are not same!")
            return redirect("registration")

    return render(request, "registration.html")


def login(request):
    return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")
