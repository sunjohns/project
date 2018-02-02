"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from untitled7 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^userlist/', views.userlist),
    url(r'^userdetail/(?P<id>\d*)/$', views.userdetail),
    url(r'^adduser/', views.adduser),
    url(r'^deluser/', views.deluser),
    url(r'^edituser/', views.edituser),
    url(r'^loginform/', views.loginByForm),
    url(r'^i/', views.i),
    url(r'^acc_login/', views.acc_login),
   # url(r'^examlogin/', views.examlogin),
    #url(r'^examlogout/', views.examlogout),
    #url(r'^$', views.examindex),
    ]
