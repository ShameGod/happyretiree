from django.http import * 
from core import utils
from django.shortcuts import *
from .models import Event, Activity
from django.contrib.auth.models import User



def list_events(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/listevents.html", {'e': Event.objects.all()})

def list_activities(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/listactivities.html", {'a': Activity.objects.all()})

def create_event(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/createactivity.html", {'a': Activity.objects.all(),'u' : User.objects.all()})