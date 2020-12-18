from django.db import models

# Create your models here.


class user(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    oname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
