# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#下面这三句一定要写，为了实现评论功能，和detail下的{% load comments %}结合就可以实现评论
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.db import models
from test.test_imageop import MAX_LEN
from django.contrib.auth.models import User


# Create your models here.
#bbs是贴子，bbs_user是用户 catagory是版块
class BBS(models.Model):
    category = models.ForeignKey('Category')#onetomany外键，因为此时Category没有创建，所以引号
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)#blank是true，就是你在admin后台使用时，可以空，null的话就是在数据库里操作可以空
    content = models.TextField()
    author = models.ForeignKey('BBS_user')#外键
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)#添加后时间不变
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user')

    def __unicode__(self):
        return self.name


class BBS_user(models.Model):
    user = models.OneToOneField(User)#onetoone就是一个user只能和一个root配对，反正以后关于用户的你都这样，因为User是内置表，就不用引号
    signature = models.CharField(max_length=128, default='This guy is too lazy to levave anything here.')
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user-1.jpg")#默认把照片传到该目录下

    def __unicode__(self):
        return self.user.username#user是一个对象，你要看user表里的username

#我们pip install pillow
# pip install django_contrib_comments
# python manage.py makemigrations
# python manage.py migrate
#登录admin你就会发现多了五张表，此时数据库表结构创建完成，开始后续操作

