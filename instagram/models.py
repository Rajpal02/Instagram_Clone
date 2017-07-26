# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Customaddons.models import BaseModel

# Create your models here.
class UserModels(BaseModel):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
