from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def editing_note(request):
    return render(request, 'core/editing_note.html')

def about(request):
    return render(request, 'core/about.html')