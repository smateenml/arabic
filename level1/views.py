from django.shortcuts import render, HttpResponse

def conjugation(request):
    return render(request, 'level1/conjugation.html', {})