from django.contrib import admin
from django.urls import path,include
from website.views import *

app_name='website'

urlpatterns = [
    path('',website_view,name='website_index'),
    path('pricing/',pricing_view,name='pricing')
]