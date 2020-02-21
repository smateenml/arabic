from django import forms
from level1.models import Conjugation

class ConjugationCreateForm(forms.ModelForm):
    class Meta:
        model = Conjugation
        fields = ['he_past','she_past','you_male_past','you_female_past','i_past','we_past',
        'he_present','she_present','you_male_present','you_female_present','i_present','we_present',
        'meaning','usage','comment']