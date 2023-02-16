from django.urls import path
from django.urls import re_path as url
from . import controller
from django.shortcuts import *

app_name="core"

urlpatterns = [ 
    url(r'^api/users$', controller.userSdk),
    url('login', controller.login_user, name="login"),
    url('signup', controller.signup_user, name="signup"),
    url('logout', controller.logout_user, name="logout"),
    url('home', controller.homepage, name="home")
]
