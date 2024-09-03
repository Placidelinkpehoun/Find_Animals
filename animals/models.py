from django.db import models

class Image(models.Model):
    id_image = models.IntegerField(unique=True, primary_key=True)
    caracteristique = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
