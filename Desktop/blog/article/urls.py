from django.contrib import admin
from django.urls import path,include
from . import views


app_name = "article"

urlpatterns = [
    path("create/",views.about,name = "about"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("addarticle/",views.addArticle,name = "addarticle"),
]