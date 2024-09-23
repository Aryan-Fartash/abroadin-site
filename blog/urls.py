from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('',blog_view,name='blog_index'),
    path('4-challenges-international-students-face-in-the-us',challenges_international_students_view,name='4-challenges-international-students'),
    path('4-sources-to-find-scholarships-in-europe',challenges_international_students_europe_view,name='challenges-international-students-europe'),
]