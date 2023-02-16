from django.shortcuts import *
from django.contrib import messages

app_name="event"

def isLogged(request):
    return "logged_in" in request.session

def redirectWithError(request, msg):
    messages.error(request=request, message=msg)
    return render(request, "authentication/login.html")
def redirectWithSuccess(request):
    messages.success(request=request, message="you are already logged")
    return render(request, "pages/home.html")