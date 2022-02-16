from django.shortcuts import render
from .forms import *
from .classes import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches


def home(request):
    return render(request, 'calculate/home.html')


def square(request):
    x = 0
    fom = OneForm()
    perimetr = 0
    area = 0
    Square(x).draw()
    if request.method == 'POST':
        fom = OneForm(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                Square(x).draw()
                area = Square(x).get_area()
                perimetr = Square(x).get_perimetr()
            except ValueError:
                fom = OneForm()
                area = "Error"
                perimetr = "Error"
    data = {'fom': fom, 'perimetr': perimetr, 'area': area}
    return render(request, 'calculate/square.html', data)


def rectangle(request):
    x = 0
    y = 0
    fom = TwoForms()
    perimetr = 0
    area = 0
    Rectangle(x, y).draw()
    if request.method == 'POST':
        fom = TwoForms(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                y = fom.cleaned_data['side_y']
                Rectangle(x, y).draw()
                area = Rectangle(x, y).get_area()
                perimetr = Rectangle(x, y).get_perimetr()
            except ValueError:
                fom = TwoForms()
                area = "Error"
                perimetr = "Error"
    data = {'fom': fom, 'perimetr': perimetr, 'area': area}
    return render(request, 'calculate/rectangle.html', data)


def circle(request):
    x = 0
    fom = OneForm()
    diametr = 0
    area = 0
    circumference = 0
    Circle(x).draw()
    if request.method == 'POST':
        fom = OneForm(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                Circle(x).draw()
                area = Circle(x).get_area()
                diametr = Circle(x).get_diametr()
                circumference = Circle(x).get_circumference()
            except ValueError:
                fom = OneForm()
                area = "Error"
                diametr = "Error"
                circumference = "Error"
    data = {'fom': fom, 'diametr': diametr, 'area': area, 'circumference': circumference}
    return render(request, 'calculate/circle.html', data)


def triangle(request):
    x = 0
    fom = OneForm()
    perimetr = 0
    area = 0
    median = 0
    Triangle(x).draw()
    if request.method == 'POST':
        fom = OneForm(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                Triangle(x).draw()
                area = Triangle(x).get_area()
                perimetr = Triangle(x).get_perimetr()
                median = Triangle(x).get_median()
            except ValueError:
                fom = OneForm()
                area = "Error"
                perimetr = "Error"
                median = "Error"
    data = {'fom': fom, 'perimetr': perimetr, 'area': area, 'median': median}
    return render(request, 'calculate/triangle.html', data)


def rombus(request):
    x = 0
    y = 0
    fom = TwoForms()
    perimetr = 0
    area = 0
    Rombus(x, y).draw()
    if request.method == 'POST':
        fom = TwoForms(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                y = fom.cleaned_data['side_y']
                Rombus(x, y).draw()
                area = Rombus(x, y).get_area()
                perimetr = Rombus(x, y).get_perimetr()
            except ValueError:
                fom = TwoForms()
                area = "Error"
                perimetr = "Error"
    data = {'fom': fom, 'perimetr': perimetr, 'area': area}
    return render(request, 'calculate/rombus.html', data)


def trapezoid(request):
    x = 0
    y = 0
    z = 0
    fom = ThreeForms()
    area = 0
    diagonal = 0
    Trapezoid(x, y, z).draw()
    if request.method == 'POST':
        fom = ThreeForms(request.POST)
        if fom.is_valid():
            try:
                x = fom.cleaned_data['side_x']
                y = fom.cleaned_data['side_y']
                z = fom.cleaned_data['side_z']
                Trapezoid(x, y, z).draw()
                area = Trapezoid(x, y, z).get_area()
                diagonal = Trapezoid(x, y, z).get_diagonal()
            except ValueError:
                fom = ThreeForms()
                area = "Error"
                diagonal = "Error"
    data = {'fom': fom, 'diagonal': diagonal, 'area': area}
    return render(request, 'calculate/trapezoid.html', data)


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
