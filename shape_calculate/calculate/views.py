from django.shortcuts import render


def layout(request):
    return render(request, 'calculate/layout.html')


def index(request):
    return render(request, 'index.html')