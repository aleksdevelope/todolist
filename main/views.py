from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def editing_note(request):
    return render(request, 'main/editing_note.html')


def about(request):
    return render(request, 'main/about.html')
