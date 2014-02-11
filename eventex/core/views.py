# coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.conf import settings

# Create your views here.

def home(request):
	return render(request,'index.html')
	#context = {'STATIC_URL': settings.STATIC_URL}
	#context = RequestContext(request)
	#return render_to_response('index.html', context)
	#t = loader.get_template('index.html')
	#c = Context()
	#content = t.render(c)
	#return HttpResponse(content)




