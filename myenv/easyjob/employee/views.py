from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def employee(request):
	return HttpResponse("<h1>i am employee app</h1>")

def employee1(request):
	return HttpResponse("<h1>i am employee1 app</h1>")

def employee2(request):
	return HttpResponse("<h1>i am employee2 app</h1>")
# Create your views here.
