from django.shortcuts import render, HttpResponse
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from level1.models import Conjugation
from level1.forms import ConjugationForm

def conjugation(request):

    conjugations = Conjugation.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')

        if search:
            conjugations = Conjugation.objects.filter(Q(he_past__icontains=search)|Q(she_past__icontains=search)|Q(you_male_past__icontains=search)|Q(you_female_past__icontains=search)|Q(i_past__icontains=search)|Q(we_past__icontains=search)|Q(he_present__icontains=search)|Q(she_present__icontains=search)|Q(you_male_present__icontains=search)|Q(you_female_present__icontains=search)|Q(i_present__icontains=search)|Q(we_present__icontains=search)|Q(meaning__icontains=search))
        
    return render(request, 'level1/conjugation.html', {'conjugations': conjugations})

class ConjugationCreate(CreateView):
    model = Conjugation
    form_class = ConjugationForm
    success_url = reverse_lazy('level1:conjugation')

class ConjugationUpdate(UpdateView):
    model = Conjugation
    form_class = ConjugationForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('level1:conjugation')

class ConjugationDelete(DeleteView):
    model = Conjugation
    form_class = ConjugationForm
    success_url = reverse_lazy('level1:conjugation')