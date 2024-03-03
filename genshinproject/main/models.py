from django.db import models

class Characters(models.Model):
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    rare = models.CharField(max_length=255)
    element = models.CharField(max_length=255)
    vide_link = models.CharField(blank=True, max_length=1000)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")

    def __str__(self):
        return self.title