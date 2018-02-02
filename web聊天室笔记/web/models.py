
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User#我们一开始要导入User表，用于外键使用

class ChatRoom(models.Model):#每个房间的记录表
    name=models.CharField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name
class ChatAccount(models.Model):#每个房间的用户都记录在这个表，又同时记录所有房间
    room=models.ForeignKey(ChatRoom)#该字段对应外键表ChatRoom，该room可以引用出ChatRoom的所有字段
    user=models.ForeignKey(User)#该user字段可以引用外键表User的所有字段包括Username，Password
    def __unicode__(self):
        return self.room

