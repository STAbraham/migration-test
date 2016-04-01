from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50, default='')
    telephone_number = models.BigIntegerField(null=True)

class Friends(models.Model):
    person = models.ForeignKey(Person, related_name="person")
    friend = models.ForeignKey(Person, related_name="friend")

class NewDB(models.Model):
    adhagh = models.CharField(max_length=30)
    friends = models.ForeignKey(Friends)