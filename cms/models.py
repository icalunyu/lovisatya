import uuid
import os
from django.db import models

# Create your models here.
class Rsvp(models.Model):
    ATTENDING_CHOICES = (
        # (value, (""))
        ('', ('You are attending ....')),
        ('all', ('All')),
        ('reception', ('Reception')),
        ('party', ('Dinner & Party'))
    )

    GUEST_CHOICES = (
        # (value, (""))
        ('', ('Will you bring plus one?')),
        ('notalone', ('Yes, I Will.')),
        ('alone', ('No. I`m coming alone')),
    )

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    guest = models.CharField(max_length=255, choices = GUEST_CHOICES)
    attending = models.CharField(max_length=255, choices = ATTENDING_CHOICES)
    keypass = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

class Code(models.Model):

    def __str__(self):
        return self.code

    code = models.CharField(max_length=255)
