from django.db import models

# Create your models here.
class Blog(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
