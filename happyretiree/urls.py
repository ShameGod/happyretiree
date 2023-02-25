"""happyretiree URL Configuration"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('event/', include("event.urls")),
    path('core/', include("core.urls")),
    path('admin/', admin.site.urls),
]

admin.site.site_header="HAPPY RETIREE"
admin.site.site_title="Welcome to the happy retiree web site"
admin.site.index_title="Share your hobbies and work together"