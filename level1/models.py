from django.db import models

class Conjugation(models.Model):
    he_past = models.CharField(max_length=500)
    she_past = models.CharField(max_length=500)
    you_male_past = models.CharField(max_length=500)
    you_female_past = models.CharField(max_length=500)
    i_past = models.CharField(max_length=500)
    we_past = models.CharField(max_length=500)

    he_present = models.CharField(max_length=500)
    she_present = models.CharField(max_length=500)
    you_male_present = models.CharField(max_length=500)
    you_female_present = models.CharField(max_length=500)
    i_present = models.CharField(max_length=500)
    we_present = models.CharField(max_length=500)
    
    # he_future = models.CharField(max_length=500)
    # she_future = models.CharField(max_length=500)
    # you_male_future = models.CharField(max_length=500)
    # you_female_future = models.CharField(max_length=500)
    # i_future = models.CharField(max_length=500)
    # we_future = models.CharField(max_length=500)

    meaning = models.CharField(max_length=500)
    usage = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.he_past

    def getHePast(self):
        return self.he_past + 'هو'