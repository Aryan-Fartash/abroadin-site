from django.shortcuts import render
from django.http import HttpResponse

def website_view(request):
    return render(request,'website/index.html')

