
from django.contrib import admin
from django.urls import path 
from app.views import *

urlpatterns = [
    path("<team>", leadership, name="leaderships"),
    path("", homepage, name="home"),
    path("admin/", admin.site.urls),
]
