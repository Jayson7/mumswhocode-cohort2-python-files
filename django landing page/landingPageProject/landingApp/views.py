from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

# class based views 
# function based views


def homepage(request):
    
    return render(request, 'index.html')

