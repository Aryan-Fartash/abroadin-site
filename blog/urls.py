from django.contrib import admin
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import *

urlpatterns = [
    path('',blog_view,name='blog_index'),
    path('4-challenges-international-students-face-in-the-us',challenges_international_students_view,name='4-challenges-international-students'),
    path('4-sources-to-find-scholarships-in-europe',challenges_international_students_europe_view,name='challenges-international-students-europe'),
    path('5-challenges-of-international-students-in-canada',challenges_international_students_canada_view,name='challenges-international-students-canada'),
]
urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))