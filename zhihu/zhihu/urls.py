"""zhihu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from zhihu.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^$',home),
    url(r'^time/$',time),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^currentTime/$',current_datetime),
    url(r'^daily/$',daily),
    url(r'^daily/time/(\d{1,8})/$',daily_time),
    url(r'^info/$',info),
    url(r'^search/$',search),
    url(r'^search-form/$',search_form),
    url(r'^craw-daily/$',craw_daily),
    url(r'^json/$',json_test),
    url(r'^daily/select/$',daily_search),
]
