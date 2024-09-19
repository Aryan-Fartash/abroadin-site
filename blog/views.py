from django.shortcuts import render
from django.http import HttpResponse

def blog_view(request):
    return render(request,'blog/index.html')

def challenges_international_students_view(request):
    return render(request,'blog/4-challenges-international-students-face-in-the-us.html')

