from django.contrib import admin

from django.contrib import admin
from .models import *

modelList =[Activity, Event]
admin.site.register(modelList)