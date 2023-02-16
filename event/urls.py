from django.urls import path
from django.urls import re_path as url
from . import controller
from django.shortcuts import *


urlpatterns = [ 
    url('listevents', controller.list_events, name="list_events"),
    url('listactivities', controller.list_activities, name="list_activities"),
    url('createevent', controller.create_event, name="create_event"),
    #url('createactivity', controller.create_activity, name="create_activity"),
    
]
