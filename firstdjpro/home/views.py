from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("index function is running")
    return HttpResponse("<h1>index function is running</h1>")
def programmers(request):
    return HttpResponse("<h1>welcome to programmers point</h1>")