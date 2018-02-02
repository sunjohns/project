# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.

def hello(request):
     s="hello world"
     current_time=datetime.datetime.now()
     html='<html><head></head><body><h1>%s</h1><p>%s</p></body></html>'%(s,current_time)
     return HttpResponse(html)
def login(request):
     return render_to_response("index.html")
def Auth(request):
     print request.GET
     user,passwd=request.GET['username'],request.GET['password']
     if user=='sunjohn' and passwd=='183016':
          return HttpResponse('welcome to our network %s,%s'%(user,passwd))
     else:
          return HttpResponse('wrong username or wrong password!!!')
def Menu(request):
     region_dic={
          "shandong":{'JiNan':['jining','hhh','baichi']},
          "HeNan":{'XinYang':['leling']},
          "FuJian":{'NingDe':['xiapu','fuan']}
     }
     return HttpResponse(json.dumps(region_dic))






