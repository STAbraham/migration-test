from __future__ import unicode_literals

from django.db import models

from migration.models import Person

# Create your models here.
class Test1(models.Model):
  blahblah = models.CharField(max_length=235)
  tatata = models.CharField(max_length=123)

class Test3(models.Model):
    link_to_people = models.ForeignKey(Person)
    trait = models.CharField(max_length=40)
    traitnum = models.BigIntegerField(null=True)

class University(models.Model):
    university_name = models.CharField(max_length=40)
    university_address = models.CharField(max_length=40)
    university_telephone_number = models.BigIntegerField(null=True)

class Class_Directory(models.Model):
    person = models.ForeignKey(Person, null=True)
