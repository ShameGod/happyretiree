from django.urls import path
from django.urls import re_path as url
from . import controller
from django.shortcuts import *


urlpatterns = [ 
    url('listevents', controller.list_events, name="list_events"),
    url('listactivities', controller.list_activities, name="list_activities"),
    url('createEvent', controller.create_event, name="create_event"),
    url('createActivity', controller.create_activity, name="create_activity"),
    url('myEvents', controller.list_my_events, name="list_my_events"),
    path('deleteEvent/<int:eventId>/', controller.delete_event, name="delete_event"),
    path('updateEvent/<int:eventId>/', controller.update_event, name="update_event"),
    
]
