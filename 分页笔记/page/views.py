# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from page.models import UserInfo
from htmlhelper import pagerhelper#要导入自己写的模块
from page.models import *

def index(request,page=1):#给他一个默认值1
    """ for i in range(315):
        userinfo=UserInfo(Name='sunjohn'+str(i),Email='sunjohn@live.com'+str(i),Phone='3838335')
        userinfo.save()
    """#先利用该for循环创建很多数据，然后把这个循环注释
    page=int(page)
    totalnum=UserInfo.objects.all().count()#得到该表的所有数据的数量
    p=pagerhelper.page('/index/',totalnum,page)#然后去调用自己写的模块的page方法，page方法要求传入三个参数
    return render_to_response('index.html',{'page':p})#把从page方法得到的返回值p，作为模版语言放到index页面

