from django.urls import path
from . import views

app_name="level1"
urlpatterns = [
    path('conjugation/', views.conjugation, name='conjugation'),
]