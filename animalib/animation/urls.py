from django.urls import path
from . import views

app_name = 'animation'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('animation/', views.animation, name='animation'),
    path('documentation/', views.documentation, name='documentation'),
]
