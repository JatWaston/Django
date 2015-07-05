# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello,home,current_date,hours_ahead,offsettest,test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),#^匹配字符串开头，$匹配字符串结尾
    url(r'^$',home),
    url(r'^time/$',current_date),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^offset/.*',offsettest),
    url(r'^test/$',test),
)
