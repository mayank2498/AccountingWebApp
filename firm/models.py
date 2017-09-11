from __future__ import unicode_literals
from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=500)
    year = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default="mayank")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name
