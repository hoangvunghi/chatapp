from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def frontpage(request):
    if request.user.is_authenticated:
        return redirect("rooms")
    else:
        return render(request, "core/frontpage.html")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect("frontpage")
    else:
        form = SignUpForm()

    return render(request, "core/register.html", {"form": form})