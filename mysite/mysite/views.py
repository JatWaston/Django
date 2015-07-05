#-*- coding: UTF-8 -*-

__author__ = 'JatWaston'

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response

import datetime

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def hello(request):
	print sys.path
	if request.method == 'GET':
		print 'GET'
	return HttpResponse('Hello World')

def home(request):
	return HttpResponse('Home')

def current_date(request):
	now = datetime.datetime.now()
	# html = '<html><body>北京时间:%s.</body></html>' % now
	# return HttpResponse(html)
	#使用模版
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):

	now = datetime.datetime.now()
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = now + datetime.timedelta(hours=offset)
	# assert False
	# html = "<html><body>再过%s小时的时间为%s.</body></html>" % (offset,dt)
	# return HttpResponse(html)

	#使用模版
	return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})

def offsettest(request,offset):
	html = "<html><body>offset:%s</body></html>" % offset
	return HttpResponse(html)

def test(request):
	return render_to_response('mypage.html',{'title':'mypage','current_section':'nav'})
	# return render_to_response('mypage.html',{'title':'mypage',})

