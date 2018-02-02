#coding=utf-8
from untitled7.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django import forms
#from django.template import RequestContext
#from django.views.decorators.csrf import csrf_protect
from untitled7.HtmlHelper import Pager#Pager是从自己写的帮助文档导入
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect


class LoginForm(forms.Form):
    username = forms.CharField(max_length=3)
    password = forms.CharField(max_length=3,widget=forms.PasswordInput())



#def model(request):
   # p=Student(name='shabi')
    #p.save()
   # p.name='tang'
    #p.save()
    #modell=Student.objects.get(id=1)
   # d=Student.objects.filter(id=1).update(name='sunjohn')
   # a = Student.objects.filter(name__contains='a').count()
    #c = Student.objects.filter(name__contains='a')[1:3]
    #c = Student.objects.values('name')

    #return render_to_response('index.html',{'key':'sunjohn'})
#@csrf_protect
def login(request):
    data={'loginstatu':''}
    if request.method=="POST":
        postdata=request.POST
        username=postdata.get('username')
        password=postdata.get('password')
        if username and password:
           if Student.objects.get(Username=username,Password=password):
                   return redirect('/index/')
           data['loginstatu']='cuowu'
    return render_to_response('login.html',data)
def index(request):
    return render_to_response('index.html')

#@csrf_protect
def userlist(request):
    result=Student.objects.all()
    page=Pager('http://127.0.0.1:8000/userlist/',2,90,180,20)#这些数字就是当前页，记录量等
    return render_to_response('userlist.html', {'model': result,'page':page})
def userdetail(request,id):
    result=Student.objects.get(Nid=int(id))
    return render_to_response('userdetail.html',{'key':result})
def adduser(request):#包括下面的增删查改都是根据前端定义的name来进行数据库操作
    postData=request.POST
    username=postData.get('username')
    password=postData.get('password')
    if username and password:

            student = Student(Username=username, Password=password)
            student.save()
    return redirect('/userlist/')#跳转
def deluser(request):
    postdata=request.POST
    nid=postdata.get('delnid')
    nid=int(nid)
    b=Student.objects.filter(Nid=nid)
    b.delete()
    return redirect('/userlist/')
def edituser(request):
    postdata=request.POST
    username=postdata.get('username')
    password=postdata.get('password')
    nid=postdata.get('did')
    nid=int(nid)
    b=Student.objects.filter(Nid=nid)
    b.update(Username=username,Password=password)
    return redirect('/userlist/')
def loginByForm(request):
    data = request.POST
    loginForm = LoginForm(data)
    if loginForm.is_valid():
        return HttpResponse('ok')
    return render_to_response('loginform.html',{'model':loginForm})
def i(request):
    hanxin='sunjohn'
    #raise Exception(hanxin)
    return HttpResponse(hanxin)
def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    student = auth.authenticate(Username=username,Password=password)
    print username,password
    if student is not None:
        auth.login(request,student)
        content = '''
              Welcome %s !!!

              <a href='/logout/' >Logout</a>

               ''' %student.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('examlogin.html',{'login_err':'cuowu'})



#def examlogin(request):
     #   return render_to_response('examlogin.html')


#这的装饰器是前面导入的，放到index界面，并且url要有#url(r'^account/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
#然后此时装饰器是只有你登录才能访问index，其他时候访问不了，没有装饰器，就到index页面，如果有装饰器，就到认证页面，最后认证成功才跳转到index页面
#@login_required
#def examindex(request):
 #   return render_to_response('examindex.html',{'student': request.student})

#def examlogout(request):
   # student = request.student
   # auth.logout(request)
   # # Redirect to a success page.
   # return HttpResponse("<b>%s</b> logged out! <br/><a href='/examindex/'>Re-login</a>" % student)


