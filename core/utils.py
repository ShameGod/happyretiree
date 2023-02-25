from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import *
from . import constants

app_name="event"

### PAGE RENDERING:
def renderHomePage(request, dict):
    return render(request, "pages/home.html", dict)
def renderSignupPage(request):
    return render(request, "authentication/signup.html")

### User SDK: TODO: add error handling*
def createUser(request):
    """
    createUser creates a new normal user (NOT STAFF)
    """
    user=User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
    user.first_name=request.POST["first_name"]
    user.last_name=request.POST["last_name"]
    user.save()
    return user 

def logUser(request):
    """"
    logUser Logs the user and adds some variables to the session
    """
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session["logged_in"]=True
        return redirect("/core/pages/home.html")
    else: 
        messages.error(request=request, message=constants.WRONG_CREDENTIALS)
        return redirect("/core/authentication/login.html")

def isLogged(request):
    return "logged_in" in request.session
def redirectWithError(request, msg):
    messages.error(request=request, message=msg)
    return redirect("/core/authentication/login.html")
def redirectWithSuccess(request):
    messages.success(request=request, message="you are already logged")
    return renderHomePage(request, None)