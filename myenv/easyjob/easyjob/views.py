from django.shortcuts import render
from slider.models import Slider
from company.models import Vacancy,CompanyProfile
from blog.models import Blog
from django.db.models import Q
from django.contrib import messages
from employee.models import EmployeeProfile,Skill
import re, math
import numpy as np
import pandas as pd
from collections import Counter
WORD = re.compile(r'\w+')



def index(request):
	try:
		if request.user.is_authenticated():
			employee=EmployeeProfile.objects.get(user_id=request.user.id)
			myskill=Skill.objects.filter(employee_id=employee.id)
			myjob=Vacancy.objects.all()
			myid=myfilterid(myskill,myjob)
			myjob=Vacancy.objects.filter(id__in=myid)
		else:
			print("not login")
			myjob=Vacancy.objects.all()[:5]
	except:
		print("error occur")
		myjob=Vacancy.objects.all()


	context={
	'slider':Slider.objects.all(),
	'vacancy':myjob,
	}
	return render(request,'index.html',context)


def blog(request):
	blog={
	'blog':Blog.objects.all(),
	}
	return render(request,'blog.html',blog)


def search(request):
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match=Vacancy.objects.filter(Q(title__icontains=srch)|
			                             Q(vacancy_location__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('search')
    return render(request,'search.html')

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def myfilterid(myskill,myjob):
    m=""
    joblist_id=[]
    cosine_value =[]
    for x in myskill:
        m=x.skill+" "+m
    vector1 = text_to_vector(m)
    for x in myjob:
        joblist_id.append(x.id)
        a = text_to_vector(x.title.split()[0]+","+x.tag)
        cosine_value.append(get_cosine(vector1,a))
    print(cosine_value)
    index = list(range(0,len(joblist_id)))
    df = pd.DataFrame({'id':joblist_id,'cosine':cosine_value},index=index)
    df = df[(df['cosine']>0.1)]
    myid = df['id'].values
    myid=myid.tolist()
    return myid
