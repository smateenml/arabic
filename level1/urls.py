from django.urls import path
from . import views


urlpatterns = [
    path('conjugation/', views.conjugation, name='conjugation'),
]