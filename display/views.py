from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from display.models import UserProfile
from display.form import WriteForm, FolderForm
from display.form import FolderForm
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
            if UserProfile.objects.filter(username=name).exists():
                messages.info(request, "Username already exist!")
                return redirect("registration")

            if UserProfile.objects.filter(email=email).exists():
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
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=name, password=password)

        if user:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Couldn't find your account")
            return redirect("login")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


def folder(request):
    f = FolderForm()
    if request.method == "POST":
        f = FolderForm(request.POST, request.FILES)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.info(request, "Your work has successfully been saved")
            return redirect("/")

    return render(request, "folder.html",
                  {"folder":f})
