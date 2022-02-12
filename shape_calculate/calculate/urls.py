from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='calculate/home'),
    path('square/', views.square, name='calculate/square'),
    path('rectangle/', views.rectangle, name='calculate/rectangle'),
    path('circle/', views.circle, name='calculate/circle'),
    path('triangle/', views.triangle, name='calculate/triangle'),
    path('rombus/', views.rombus, name='calculate/rombus'),
    path('trapezoid/', views.trapezoid, name='calculate/trapezoid'),
    path('cube/', views.cube, name='calculate/cube'),
    path('parallelepiped/', views.parallelepiped, name='calculate/parallelepiped'),
    path('sphere/', views.sphere, name='calculate/sphere'),
    path('pyramid/', views.pyramid, name='calculate/pyramid'),
    path('cylinder/', views.cylinder, name='calculate/cylinder'),
    path('cone/', views.cone, name='calculate/cone'),
]
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)