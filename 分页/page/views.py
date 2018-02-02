# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from page.models import UserInfo
from htmlhelper import pagerhelper
from page.models import *

def index(request,page=1):
    """ for i in range(315):
        userinfo=UserInfo(Name='sunjohn'+str(i),Email='sunjohn@live.com'+str(i),Phone='3838335')
        userinfo.save()
    """
    page=int(page)
    totalnum=UserInfo.objects.all().count()
    p=pagerhelper.page('/index/',totalnum,page)
    return render_to_response('index.html',{'page':p})

