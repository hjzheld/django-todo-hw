from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "signup.html")
        
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            auth_login(request, user)
            return redirect("/todo/")
        else:
            return HttpResponse("Invaild auth", status=401)
    elif request.method == "GET":
        return render(request, "login.html")
    else :
        return HttpResponse("Invaild auth", status=401)
    