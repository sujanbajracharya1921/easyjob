from django.http import HttpResponse
from django.shortcuts  import render
def index(request):
	TEMPLATE_DIR='blog.html'
	context={
	'insert':1233445,
	}
	return render(request,TEMPLATE_DIR,context)
def blog(request):
	return HttpResponse("<em>Hello this is blog page</em>")