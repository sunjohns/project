# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,redirect,HttpResponse,HttpResponseRedirect

from django.contrib import auth
from web.models import *
import json

msg_dic={}#实现定义一个空字典
#格式大概是{
#        1:[[],[],[]]----1是用户id，每个id对应一个消息队列value的列表，每个value列表又包含很多不同用户的消息列表
#        }

def login(request):#因为我们有一个默认的User表，我们通过匹配得到是否我们的User表存在相同的登录的用户，是的话，就让他进入系统，并且保留登录会话
   if request.method=='post':
       username=request.POST.get('username')
       password=request.POST.get('password')

       user=auth.authenticate(username=username,password=password)#User表的Username和Password，大小写没事
       if user is not None:
           auth.login(request,user)

           return HttpResponseRedirect('/index/')

       else:
           login_error='cuowu'
           return render_to_response('login.html',{'login_error':login_error})
   return render_to_response('login.html')


def index(request):
   rooms=ChatRoom.objects.all()#用户登录后，会看到房间所有ChatRoom表的room
   return render_to_response('index.html',{'room_content':rooms,'user':request.user})
def detail(request,id):
   roomobj=ChatRoom.objects.get(id=id)#根据每个room的id，得到相应room的对象
   result=ChatAccount.objects.filter(room=roomobj,user=request.user)#查看CharAccount表是否有用户是当前登录用户，房间是用户选择房间的记录，如果没有就将该登录用户和房间写入该ChatAccount表
   if not result:
     c=ChatAccount(room=roomobj,user=request.user)
     c.save()
   membercount=ChatAccount.objects.filter(room=roomobj)#然后得到ChatAccount表里room是roomobj的所有用户对象记录（每个room可以很多用户）
   return render_to_response('detail.html',{'roomobj':roomobj,'membercount':membercount,'user':request.user})#还要传入当前登录的用户
def logout(request):
    pass#这个自己写嘛
def savemsg(request):#下面的都是从前端detail页面ajax过来的内容，通过post方法得到
    id,msg,sendtime,roomid,name=request.POST.get('id'),request.POST.get('msg'),request.POST.get('sendtime'),request.POST.get('roomid'),request.POST.get('name')
    if msg_dic.has_key(int(roomid)):#事先定义一个空字典，该字典我们期望的格式是，key为房间号，value为传入的其他值
        msg_dic[int(roomid)].append(id,msg,sendtime,name)#因为value是列表格式我们才方便把数据append到value列表中中变成新的用户消息小列表
    else:
        msg_dic[int(roomid)]=[[id,msg,sendtime,name],]#因为每个房间肯定很多不同用户发送数据，所以我们的value的初始值又要是列表格式，value里面定义不同用户的会话列表
    return HttpResponse('ok')
def getmsg(request):
    roomid=request.GET.get('roomid')
    msglist=[]#msglist实际就是value的列表，也和savemsg一样字典里很多列表，列表里很多小列表
    if msg_dic.has_key(int(roomid)):
       msglist=msg_dic[int(roomid)]
    return HttpResponse(json.dumps(msglist))#我们要把字典json给前端