from django.shortcuts import render
from .forms import *
from .classes import *


def home(request):
    return render(request, 'calculate/home.html')


def square(request):
    X = 0
    fom = AddPostForm()
    perimetr = 0
    area = 0
    if request.method == 'POST':
        fom = AddPostForm(request.POST)
        if fom.is_valid():
            try:
                X = fom.cleaned_data['side']
                area = Square(int(X)).area()
                perimetr = Square(int(X)).perimetr()
            except ValueError:
                fom = AddPostForm()
                area = "Error"
                perimetr = "Error"
    data = {'fom': fom, 'perimetr': perimetr, 'area': area}
    return render(request, 'calculate/square.html', data)



def rectangle(request):
    return render(request, 'calculate/rectangle.html')


def circle(request):
    return render(request, 'calculate/circle.html')


def triangle(request):
    return render(request, 'calculate/triangle.html')


def rombus(request):
    return render(request, 'calculate/rombus.html')


def trapezoid(request):
    return render(request, 'calculate/trapezoid.html')


def cube(request):
    return render(request, 'calculate/cube.html')


def parallelepiped(request):
    return render(request, 'calculate/parallelepiped.html')


def sphere(request):
    return render(request, 'calculate/sphere.html')


def pyramid(request):
    return render(request, 'calculate/pyramid.html')


def cylinder(request):
    return render(request, 'calculate/cylinder.html')


def cone(request):
    return render(request, 'calculate/cone.html')
