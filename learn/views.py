# conding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
	#return HttpResponse("Welcome,自强学堂")
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET.get('b',0)
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_to_add2(request, a, b):
	return HttpResponseRedirect(reverse('add2',  args=(a, b)))