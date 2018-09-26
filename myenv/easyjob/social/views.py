from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def social(request):
	return HttpResponse("<h1>i am social app</h1>")

def social1(request):
	return HttpResponse("<h1>i am social1 app</h1>")
# Create your views here.
