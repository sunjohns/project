# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from web import models#django.db和项目都有models

admin.site.register(models.ChatRoom)
admin.site.register(models.ChatAccount)