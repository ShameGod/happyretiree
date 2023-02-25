from django.http import * 
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.decorators import api_view
from django.contrib.auth import *
from .serializer import UserSerializer
from . import utils
from . import constants

def homepage(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, constants.PLEASE_LOGIN)
    user=get_user(request)
    return utils.renderHomePage(request,{'userName': user.get_username})

def signup_user(request):
    if utils.isLogged(request):
        return utils.redirectWithSuccess(request)
    if request.method=="POST":
        if User.objects.filter(username=request.POST["username"]).exists():
            messages.error(request=request, message=constants.USERNAME_EXISTS)
            return utils.renderSignupPage(request)
        if User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request=request, message=constants.EMAIL_EXISTS)
            return utils.renderSignupPage(request)
        utils.createUser(request)
        messages.success(request=request, message=constants.ACCOUNT_CREATED)
        request.session["logged_in"]=True
        return utils.renderHomePage(request, None)
    if request.method=="GET":
        return utils.renderSignupPage(request)

def login_user(request):
    if utils.isLogged(request):
        return utils.redirectWithSuccess(request)
    if request.method=="POST":
        return utils.logUser(request)
    if request.method=="GET": 
        return render(request, 'authentication/login.html')

def logout_user(request):
    try:    
        del request.session["logged_in"]
    except KeyError:
        pass
    messages.success(request, constants.LOGGED_OUT)
    return redirect("/core/authentication/login.html")
