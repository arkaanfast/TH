from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("level6/", views.level_6, name='level_6'),
   path("check_ans/", views.check_lvl6, name='check_ans')
]
