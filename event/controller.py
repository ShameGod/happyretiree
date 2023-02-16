from django.http import * 
from core import utils
from django.shortcuts import *
from .models import Event, Activity
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.utils import timezone

def list_events(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/listevents.html", {'e': Event.objects.all()})

def list_activities(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/listactivities.html", {'a': Activity.objects.all()})

def create_event(request):
    if request.method=="POST":
        event = Event(name=request.POST["eventName"],
            activity=Activity.objects.get(name=request.POST["activityName"]),
            createdby=User.objects.get(username=get_user(request).get_username()),
            created_on=timezone.now(),
            date=request.POST["date"])
        event.save()
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    return render(request,"event/createEvent.html", 
        {'a': Activity.objects.all(),'u' : get_user(request)})
