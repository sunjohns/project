# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,redirect,HttpResponse,HttpResponseRedirect

from django.contrib import auth
from web.models import *
import json

msg_dic={}

def login(request):
   if request.method=='post':
       username=request.POST.get('username')
       password=request.POST.get('password')

       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)

           return HttpResponseRedirect('/index/')

       else:
           login_error='cuowu'
           return render_to_response('login.html',{'login_error':login_error})
   return render_to_response('login.html')


def index(request):
   rooms=ChatRoom.objects.all()
   return render_to_response('index.html',{'room_content':rooms,'user':request.user})
def detail(request,id):
   roomobj=ChatRoom.objects.get(id=id)
   result=ChatAccount.objects.filter(room=roomobj,user=request.user)
   if not result:
     c=ChatAccount(room=roomobj,user=request.user)
     c.save()
   membercount=ChatAccount.objects.filter(room=roomobj)
   return render_to_response('detail.html',{'roomobj':roomobj,'membercount':membercount,'user':request.user})
def logout(request):
    pass
def savemsg(request):
    id,msg,sendtime,roomid,name=request.POST.get('id'),request.POST.get('msg'),request.POST.get('sendtime'),request.POST.get('roomid'),request.POST.get('name')
    if msg_dic.has_key(int(roomid)):
        msg_dic[int(roomid)].append(id,msg,sendtime,name)
    else:
        msg_dic[int(roomid)]=[[id,msg,sendtime,name],]
    return HttpResponse('ok')
def getmsg(request):
    roomid=request.GET.get('roomid')
    msglist=[]
    if msg_dic.has_key(int(roomid)):
       msglist=msg_dic[int(roomid)]
    return HttpResponse(json.dumps(msglist))