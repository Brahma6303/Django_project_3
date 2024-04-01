from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msd(request):
    return HttpResponse("<h1><marquee>msd is captain cool</marquee></h1>")

def virat(request):
    return HttpResponse("<h1>E sala cup namduuuuuuuuuuuu</h1>")

def rohit(request):
    return HttpResponse("<h1><marquee>One of the greatest batsman in the world</marquee><h1>")