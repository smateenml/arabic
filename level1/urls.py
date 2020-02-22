from django.urls import path
from level1 import views

app_name="level1"
urlpatterns = [
    path('conjugation/', views.conjugation, name='conjugation'),
    path('conjugation/create/', views.ConjugationCreate.as_view(), name='conjugation-create'),
    path('conjugation/update/<int:pk>/', views.ConjugationUpdate.as_view(), name='conjugation-update'),
    path('conjugation/delete/<int:pk>/', views.ConjugationDelete.as_view(), name='conjugation-delete'),

]