# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
class UserInfo(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)

