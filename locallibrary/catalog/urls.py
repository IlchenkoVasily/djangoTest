from django.urls import path
from . import views

urlpatterns = [
    path('', views.intdex, name='index')
]
