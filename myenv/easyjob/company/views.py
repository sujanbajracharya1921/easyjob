from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyProfile
from .models import Vacancy
# Create your views here.
def company(request):
	context={
	'company':CompanyProfile.objects.all(),
	}
	return render(request,'index.html',context)
def company3(request):
	return HttpResponse("<h1>i am comapny app</h1>")

def company1(request):
	return HttpResponse("<h1>i am company1 app</h1>")

def company2(request):
	return HttpResponse("<h1>i am company2 app</h1>")

def vacancy(request):
	vacancy={
	'vacancy':Vacancy.objects.all()
	}
	return render(request,'vacancy.html',vacancy)