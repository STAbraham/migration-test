from django.db import models

class University(models.Model):
    university_name = models.CharField(max_length=40)
    university_address = models.CharField(max_length=40)
    university_telephone_number = models.BigIntegerField(null=True)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50, default='')
    telephone_number = models.BigIntegerField(null=True)

class Class_Directory(models.Model):
    person = models.ForeignKey(Person, null=True)

class Friends(models.Model):
    person = models.ForeignKey(Person, related_name="person")
    friend = models.ForeignKey(Person, related_name="friend")
