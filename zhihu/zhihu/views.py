# -*- coding:UTF-8 -*-

__author__ = 'JatWaston'

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from daily.models import ZhDaily
import datetime
import time
import urllib2,urllib,cookielib
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from daily.models import *
import hashlib
from zhihu import settings
import json

from django.utils.timezone import utc

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def hello(request):
	return HttpResponse("Hello World")

def home(request):
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
	today = datetime.datetime.today().replace(tzinfo=utc).strftime("%Y-%m-%d")
	print today
	return render_to_response('daily.html',{'item_list':items,'date_value':today})

def daily_time(request,timeoffset):
	try:
		timeoffset = str(timeoffset)
	except ValueError:
		raise Http404()
	print timeoffset
	oneday = datetime.timedelta(days=1)
	#要特别小心时区的问题，如果开了USE_TZ = True的话，时间转换的时候要处理时区问题
	today = datetime.datetime.strptime(timeoffset,"%Y-%m-%d").replace(tzinfo=utc) #%Y%m%d %H:%M:%S
	tomorrow = today + oneday
	#提取日期处于today和tomorrow之间的数据
	print today
	print tomorrow

	items = ZhDaily.objects.filter(publish_date__gte = today,publish_date__lt = tomorrow)
	return render_to_response('daily.html',{'item_list':items,'date_value':timeoffset})

def daily_search(request):
	if 'dateTime1' in request.GET:
		message = 'You searched for:%s' % request.GET['time']
	else:
		message = 'You submitted an empty form.'
	return daily_time(request,request.GET['time'])
	# return HttpResponse(message)


def json_test(request):
	response_data = {}
	response_data['message'] = '获取失败'
	response_data['code'] = '-1'
	return HttpResponse(json.dumps(response_data),content_type="application/json")

def info(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>%s</td></tr>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'You searched for:%s' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

def craw_daily(request):
	url = "http://daily.zhihu.com/"
	content = htmlContent(url)
	soup = BeautifulSoup(content)
	items = soup.find_all('div',attrs={'class':'box'})
	for item in items:
		# print str(item.contents)
		# print "xxxxxx"
		# print type(str(item.contents))
		contentSoup = BeautifulSoup(str(item.contents))
		imgs = contentSoup.find_all("img",attrs={"class":"preview-image"})
		if len(imgs) > 0:
			preview_img = imgs[0].get('src')
		title = contentSoup.find_all('span',attrs={'class':'title'})
		title = title[0].get_text() #获取内容
		link = contentSoup.find_all('a',attrs={'class':'link-button'})
		if len(link) > 0:
			link = link[0].get('href')
		hash = hashlib.md5()
		hash.update(link)
		time = datetime.datetime.now().replace(tzinfo=utc)
		print time
		dailyModel = ZhDaily(title=title,link=link,img=preview_img,md5=hash.hexdigest(),publish_date=time)
		dailyModel.save()
		print 'link: %s title: %s img: %s' % (link,title,preview_img)
	return HttpResponse("爬取知乎日报...")

#获取网页内容
def htmlContent(url):
	cj = cookielib.CookieJar()
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	req = urllib2.Request(url,headers=headers);
	response = urllib2.urlopen(req)
	return response.read().decode('utf-8')



