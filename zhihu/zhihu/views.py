# -*- coding:UTF-8 -*-

__author__ = 'JatWaston'

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from daily.models import ZhDaily
import datetime

def hello(request):
	return HttpResponse("Hello World")

def home(request):
	print "path: " + request.path
	print "UA:" + request.META['HTTP_USER_AGENT']
	return HttpResponse("Home Page")

def time(request):
	time = datetime.datetime.now()
	html = "<html><body>现在时间为:%s.</body></html>" % time
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>再过%s小时的时间为%s</body></html>" % (offset,dt)
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

def daily(request):
	items = ZhDaily.objects.all()
	# item = {'link':'http://daily.zhihu.com/story/4835882','title':'不同色彩的衣服，要这样搭配才好看','img':'http://pic3.zhimg.com/039ce5f86eb93eb7c0857ef775597612.jpg'}
	# item1 = {'link':'http://daily.zhihu.com/story/4840315','title':'为什么我的父母老是在吵架？','img':'http://pic1.zhimg.com/4b82d892c65de07fe416eaff5e6ac7e8.jpg'}
	# items = [item,item1]
	return render_to_response('daily.html',{'item_list':items})

def daily_time(request,time):
	items = ZhDaily.objects.all()
	return render_to_response('daily.html',{'item_list':items})



