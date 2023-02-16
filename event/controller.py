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
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    if request.method=="POST":
        event = Event(name=request.POST["eventName"],
            activity=Activity.objects.get(name=request.POST["activityName"]),
            createdby=User.objects.get(username=get_user(request).get_username()),
            created_on=timezone.now(),
            date=request.POST["date"])
        event.save()
    return render(request,"event/createEvent.html", 
        {'a': Activity.objects.all(),'u' : get_user(request)})

def create_activity(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    if request.method=="POST":
        activity = Activity(name=request.POST["activityName"],
            description=request.POST["description"],
            location=request.POST["location"]
            )
        activity.save()
    return render(request,"event/createActivity.html")

def list_my_events(request):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    user=get_user(request)
    return render(request,"event/myEvents.html", {'events': Event.objects.filter(createdby=user)})

def delete_event(request, eventId):
    if utils.isLogged(request)==False:
        return utils.redirectWithError(request, "Your session has expired")
    user=get_user(request)
    if Event.objects.get(pk=eventId).createdby==user:
        try:
            Event.objects.get(pk=eventId).delete()
            return redirect("../../myEvents")
        except:
            raise Exception("Something went wrong when deleting the event")
    return HttpResponseForbidden("This user didn't create this event so he is not authorized to edit it")