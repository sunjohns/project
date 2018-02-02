# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
import models
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django_comments.models import Comment


def index(request):
    bbs_list = models.BBS.objects.all()
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html', {
        'bbs_list': bbs_list,
        'user': request.user,
        'bbs_category': bbs_categories,
        })

def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    print '--->', bbs
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs, "user": request.user})
def Login(request):
    return render_to_response('login.html')
def base(request):
    return render_to_response('base.html')

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print username, password
    if user is not None:  # and user.is_active:
        # correct password and user is marked "active"
        auth.login(request, user)
        content = '''
         Welcome %s !!!

         <a href='/logout/' >Logout</a>

          ''' % user.username
        # return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {'login_err': 'Wrong username or password!'})

def logout(request):
        user = request.user
        auth.logout(request)
        # Redirect to a success page.
        return HttpResponse("<b>%s</b> logged out! <br/><a href='/login/'>Re-login</a>" % user)


def sub_comment(request):
    print  request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')

    Comment.objects.create(
        content_type_id=8,
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )
    return HttpResponseRedirect('/detail/%s' % bbs_id)
def bbs_pub(request):
    return render_to_response('bbs_pub.html')
def bbs_sub(request):
    print ',==>', request.POST.get('content')
    content=  request.POST.get('content')
    author = models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
        title = 'TEST TITLE',
        summary = 'HAHA',
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,
        category_id=2,

           )
    return HttpResponse('yes.')
def category(request,cata_id):
    bbs_list = models.BBS.objects.filter(category__id=cata_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',
                               {'bbs_list':bbs_list,
                                 'user':request.user,
                                 'bbs_category':bbs_categories,
                                 'cata_id': int(cata_id),
                              })