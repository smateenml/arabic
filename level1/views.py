from django.shortcuts import render, HttpResponse
from level1.models import Conjugation

def conjugation(request):
    conjugations = Conjugation.objects.all()
    return render(request, 'level1/conjugation.html', {'conjugations': conjugations})