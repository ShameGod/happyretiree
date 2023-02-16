from django.http import * 
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.decorators import api_view
from django.contrib.auth import *
from .serializer import UserSerializer
from . import utils
def homepage(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Please login")
    user=get_user(request)
    return render(request, "pages/home.html", {'userName': user.get_username})

def signup_user(request):
    if utils.isLogged(request):
        return utils.redirectWithSuccess(request)
    if request.method=="POST":
        if User.objects.filter(username=request.POST["username"]).exists():
            messages.error(request=request, message="the username already exists")
            return redirect("signup.html")
        if User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request=request, message="the email already exists")
            return redirect("signup.html")

        user=User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
        user.first_name=request.POST["first_name"]
        user.last_name=request.POST["last_name"]
        messages.success(request=request, message="Your account was created successfully")
        request.session["logged_in"]=True
        return redirect("home.html")
    if request.method=="GET":
        #TODO: check if the user is already logged in 
        return render(request, "authentication/signup.html")

def login_user(request):
    if utils.isLogged(request):
        return utils.redirectWithSuccess(request)
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["logged_in"]=True
            return redirect("home.html")
        else: 
            messages.error(request=request, message="wrong username or password")
            return redirect("authentication/login.html")
    if request.method=="GET": 
        return render(request, 'authentication/login.html')

def logout_user(request):
    try:    
        del request.session["logged_in"]
    except KeyError:
        pass
    messages.success(request, "you logged out")
    return redirect("login.html")


@api_view(['GET', 'POST', 'DELETE'])
def userSdk(request):
    if request.method=='GET':
        users= User.objects.all()
        response= UserSerializer(users, many=True)
        return HttpResponse(response)
