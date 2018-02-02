# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
import models
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django_comments.models import Comment#这个一定要写，后面才能添加评论


def index(request):
    bbs_list = models.BBS.objects.all()#得到所有bbs贴子内容，并且传到前端index.html
    bbs_categories = models.Category.objects.all()#本来都不要models，如果我们from BBS.models import*
    return render_to_response('index.html', {
        'bbs_list': bbs_list,
        'user': request.user,#没有登录就登录，此时的user为空值
        'bbs_category': bbs_categories,#把所有版块内容都显示到全部标签下
        })

def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)#得到前端index.html传来的该id的贴子
    print '--->', bbs
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs})
def Login(request):
    return render_to_response('login.html')
def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print username, password
    if user is not None:  # and user.is_active:
        # correct password and user is marked "active"
        auth.login(request, user)#保存用户登录会话
        content = '''
         Welcome %s !!!

         <a href='/logout/' >Logout</a>

          ''' % user.username
        # return HttpResponse(content)
        return HttpResponseRedirect('/')#认证通过就到index界面
    else:
        return render_to_response('login.html', {'login_err': 'Wrong username or password!'})

def logout(request):
        user = request.user#退出时返回该user
        auth.logout(request)
        # Redirect to a success page.
        return HttpResponse("<b>%s</b> logged out! <br/><a href='/login/'>Re-login</a>" % user)


def sub_comment(request):#提交评论
    print  request.POST
    bbs_id = request.POST.get('bbs_id')#从前端detailhtml页面传来的name：bbs_id
    comment = request.POST.get('comment_content')#从前端detail.html传来的name：comment_content
)

    Comment.objects.create(
        content_type_id=8,#我们现在navicat看该bbs贴子表是什么数字
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )
    return HttpResponseRedirect('/detail/%s' % bbs_id)#返回该帖子主页
def bbs_pub(request):#创建贴子
    return render_to_response('bbs_pub.html')
def bbs_sub(request):#提交贴子
    print ',==>', request.POST.get('content')
    content=  request.POST.get('content')
    author = models.BBS_user.objects.get(user__username=request.user)#BBS_user的user属性对应外键表User的username值
    models.BBS.objects.create(
        title = 'TEST TITLE',
        summary = 'HAHA',
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,
        category_id=2,#创建默认版块，’全部‘版块是id 1，后面的是2开始

           )
    return HttpResponse('yes.')
def category(request,cata_id):#版块
    bbs_list = models.BBS.objects.filter(category__id=cata_id)#BBS对应的属性category对应外键表Category的id值
    bbs_categories = models.Category.objects.all()#此时会显示该bbs所属版块的版块所有内容
    return render_to_response('index.html',
                               {'bbs_list':bbs_list,
                                 'user':request.user,
                                 'bbs_category':bbs_categories,#依然显示所有版块
                                 'cata_id': int(cata_id),#注意要int
                              })
#index和category方法，都会到index界面，一开始登录index.html显示的是全部，后来选择不同版块后，进入category方法，再次进入index.html界面，就会返回不同category的bbs贴子
#所以category和index方法放回的模版语言都有具备相同内容