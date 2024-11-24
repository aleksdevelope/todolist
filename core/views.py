from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello.")

def editing_note(request):
    return HttpResponse("Do anything.")