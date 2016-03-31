from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test1(models.Model):
  blahblah = models.CharField(max_length=235)
  tatata = models.CharField(max_length=123)

class Test2(models.Model):
  asfasdf = models.CharField(max_length=1, default='')

