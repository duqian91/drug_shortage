from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def upload(request):
    return HttpResponse("this is the upload view")