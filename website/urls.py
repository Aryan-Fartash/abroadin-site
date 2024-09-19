from django.contrib import admin
from django.urls import path,include
from website.views import *

urlpatterns = [
    path('',website_view,name='website_index'),
]