# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from BBS import models

#注册三个表，并且加入BBS_admin，这样在后台看的时候更加完美
class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__user__username')
    def signature(self,obj):#给signature重命名
        return obj.author.signature
    signature.short_description  = 'hah'


admin.site.register(models.BBS,BBS_admin)#这里一定要注意，我们要注册四个表
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
