from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('',blog_view,name='blog_index'),
]