from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import EmployeeCreateForm,SkillForm,TrainingForm,ExperienceForm,DegreeForm,CvForm,CompanyCreateForm,VacancyForm,ApplicationForm
from employee.models import EmployeeProfile,Skill,Cv
from company.models import CompanyProfile,Vacancy,Application
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):
	if request.method=='GET':
		context={
		'form':UserCreationForm(),
		}
		return render(request,'register.html',context)
	else:
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			context={
			'form':form,
			}
			return render(request,'register.html',context)

def headerprofile(request):
    if request.user.is_authenticated():
        try:
            user = EmployeeProfile.objects.get(user_id=request.user)
            return redirect('dashboard')
        except:
            company=CompanyProfile.objects.get(user_id=request.user)
            return redirect('dashboards')

    else:
        return render(request,'login.html')

def dashboard(request):
	if request.user.is_authenticated():
		return render(request,'profile.html')
	else:
		return redirect('login')

def whoareyou(request):
	if request.user.is_authenticated():
		try:
			login_user_id=request.user.id
			user=EmployeeProfile.objects.get(user_id=login_user_id)
			return redirect ('dashboard')
		except:
			try:
				company=CompanyProfile.objects.get(user_id=login_user_id)
				return redirect ('dashboards')
			except:
				return render(request,'whoareyou.html')
	else:
		return redirect ('login')

def employeeaccount(request):
	if request.method=='GET':
		context={
			'form':EmployeeCreateForm(),
			}
		return render(request,'createemployee.html',context)
	else:
		form=EmployeeCreateForm(request.POST)
		if form.is_valid():
			employee=form.save(commit=False)
			login_user_id=request.user.id
			login_user=User.objects.get(id=login_user_id)
			employee.user=login_user
			employee.save()
			return redirect('employeeskill')
		else:
			return render(request,'createemployee.html',{'form':form})

def employeeskill(request):
	if request.user.is_authenticated():
		if request.method=="GET":
			context={
				'form':SkillForm(),
				}
			return render(request,'skill.html',context)
		else:
			form=SkillForm(request.POST)
			if form.is_valid():
				skill=form.save(commit=False)
				login_user_id=request.user.id
				emp=EmployeeProfile.objects.get(user_id=login_user_id)
				skill.employee=emp
				skill.save()
				return redirect('employeetraining')
			else:
				return render(request,'skill.html',{'form':form})
	else:
		return redirect('login')


def employeetraining(request):
	if request.user.is_authenticated():
		if request.method=="GET":
			context={
				'form':TrainingForm(),
				}
			return render(request,'training.html',context)
		else:
			form=TrainingForm(request.POST)
			if form.is_valid():
				training=form.save(commit=False)
				login_user_id=request.user.id
				emp=EmployeeProfile.objects.get(user_id=login_user_id)
				training.employee=emp
				training.save()
				return redirect('employeeexperience')
			else:
				return render(request,'training.html',{'form':form})
	else:
		return redirect('login')

def employeeexperience(request):
	if request.user.is_authenticated():
		if request.method=="GET":
			context={
				'form':ExperienceForm(),
				}
			return render(request,'experience.html',context)
		else:
			form=ExperienceForm(request.POST)
			if form.is_valid():
				experience=form.save(commit=False)
				login_user_id=request.user.id
				emp=EmployeeProfile.objects.get(user_id=login_user_id)
				experience.employee=emp
				experience.save()
				return redirect('employeedegree')
			else:
				return render(request,'experience.html',{'form':form})
	else:
		return redirect('login')

def employeedegree(request):
	if request.user.is_authenticated():
		if request.method=="GET":
			context={
				'form':DegreeForm(),
				}
			return render(request,'degree.html',context)
		else:
			form=DegreeForm(request.POST)
			if form.is_valid():
				degree=form.save(commit=False)
				login_user_id=request.user.id
				deg=EmployeeProfile.objects.get(user_id=login_user_id)
				degree.employee=deg
				degree.save()
				return redirect('employeecv')
			else:
				return render(request,'degree.html',{'form':form})
	else:
		return redirect('login')

def employeecv(request):
	if request.user.is_authenticated():
		if request.method=="GET":
			context={
				'form':CvForm(),
				}
			return render(request,'cv.html',context)
		else:
			form=CvForm(request.POST,request.FILES)
			if form.is_valid():
				cv=form.save(commit=False)
				login_user_id=request.user.id
				emp=EmployeeProfile.objects.get(user_id=login_user_id)
				cv.employee=emp
				cv.save()
				return redirect('dashboard')
			else:
				return render(request,'cv.html',{'form':form})
	else:
		return redirect('login')


def companyaccount(request):
	if request.user.is_authenticated():
		if request.method=='GET':
			context={
				'form':CompanyCreateForm(),
				}
			return render(request,'createcompany.html',context)
		else:
			form=CompanyCreateForm(request.POST)
			if form.is_valid():
				company=form.save(commit=False)
				login_user_id=request.user.id
				try:
					emp=EmployeeProfile.objects.get(user_id=login_user_id)
					return render(request,'createcompany.html',{'msg':'you are already registered with employee account'})
				except:
					login_user=User.objects.get(id=login_user_id)
					company.user=login_user
					company.save()
					return redirect('dashboards')
			else:
				return render(request,'createcompany.html',{'form':form})
	else:
		return redirect ('login')


@login_required(login_url='/login/')
def updatecompany(request):
	comp=CompanyProfile.objects.get(user_id=request.user.id)
	form=CompanyCreateForm(request.POST or None,instance=comp)
	if form.is_valid():
		form.save()
		return redirect('dashboards')
	context={
		'form':form,
		}
	return render(request,'updatecompany.html',context)

def addvacancy(request):
	if request.user.is_authenticated():
		if request.method=='GET':
			context={
				'form':VacancyForm(),
				}
			return render(request,'cvacancy.html',context)
		else:
			form=VacancyForm(request.POST)
			if form.is_valid():
				vacancy=form.save(commit=False)
				login_user_id=request.user.id
				com=CompanyProfile.objects.get(user_id=login_user_id)
				vacancy.company=com
				vacancy.save()
				return redirect('allvacancy')
			else:
				return render(request,'cvacancy.html',{'form':form})
	else:
		redirect('login')

def allvacancy(request):
	if request.user.is_authenticated():
		company=CompanyProfile.objects.get(user_id=request.user.id)
		vacancy=Vacancy.objects.filter(company_id=company.id)
		context={
			'vacancy':vacancy
		}
		return render(request,'allvacancy.html',context)
	else:
		return redirect('login')


def dashboards(request):
	if request.user.is_authenticated():
		return render(request,'dashboards.html')
	else:
		return redirect('login')

def readmore(request,id):
	context={
	'vacancy':Vacancy.objects.get(id=id),
	}
	return render(request,'readmore.html',context)

def updatevacancy(request,id):
	if request.user.is_authenticated():
		vacancy=Vacancy.objects.get(id=id)
		form=VacancyForm(request.POST or None,instance=vacancy)
		if form.is_valid():
			form.save()
			return redirect('allvacancy')
		context={
			'form':form,
			}
		return render(request,'updatevacancy.html',context)
	else:
		return redirect('login')
	# vacancy=Vacancy.objects.get(id=id)
	# form=VacancyForm(instance=vacancy)
	# if request.user.is_authenticated():
	# 	if request.method=='GET':
	# 		context={
	# 		'form':form
	# 		}
	# 		return render(request,'updatevacancy.html',context)
	# 	else:
	# 		form=VacancyForm(request.POST)
	# 		if form.is_valid():
	# 			form.save()
	# 			return redirect('allvacancy')
	# 		else:
	# 			return render(request,'updatevacancy.html',context)
	# else:
	# 	return redirect('login')

def deletevacancy(request,id):
	try:
		vacancy=Vacancy.objects.get(id=id)
		vacancy.delete()
		return redirect('allvacancy')
	except:
		return redirect('allvacancy')

@login_required(login_url='/login/')
def updateuser(request):
	emp=EmployeeProfile.objects.get(user_id=request.user.id)
	form=EmployeeCreateForm(request.POST or None,instance=emp)
	if form.is_valid():
		form.save()
		return redirect('dashboard')
	context={
		'form':form,
		}
	return render(request,'updateuser.html',context)

@login_required(login_url='/login/')
def updateuserskill(request):
	if request.method=="GET":
		form=SkillForm()
		emp=EmployeeProfile.objects.get(user_id=request.user.id)
		skill=Skill.objects.filter(employee_id=emp.id)
		context={
			'form':form,
			'skill':skill
			}
		return render(request,'updateuserskill.html',context)
	else:
		form=SkillForm(request.POST)
		emp=EmployeeProfile.objects.get(user_id=request.user.id)
		skill=Skill.objects.filter(employee_id=emp.id)
		if form.is_valid():
			skill=form.save(commit=False)
			skill.employee=emp
			skill.save()
			return redirect('updateuserskill')
		else:
			return render(request,'updateuserskill.html',{'form':form,'skill':skill})

@login_required(login_url='/login/')
def deleteuserskill(request,id):
	try:
		skill=Skill.objects.get(id=id)
		skill.delete()
		return redirect('updateuserskill')
	except:
		return redirect('updateuserskill')

@login_required(login_url='/login/')
def user_cv(request):
	if request.method=="GET":
		form=CvForm()
		emp=EmployeeProfile.objects.get(user_id=request.user.id)
		cv=Cv.objects.filter(employee_id=emp.id)
		context={
			'form':form,
			'cv':cv,
		}
		return render(request,'user_cv.html',context)
	else:
		emp=EmployeeProfile.objects.get(user_id=request.user.id)
		cv=Cv.objects.filter(employee_id=emp.id)
		form=CvForm(request.POST,request.FILES)
		if form.is_valid():
			cv=form.save(commit=False)
			cv.employee=emp
			cv.save()
			return redirect('user_cv')
		else:
			return redirect(request,'user_cv.html',{'form':form,'cv':cv})

@login_required(login_url='/login/')
def deleteusercv(request,id):
	try:
		cv=Cv.objects.get(id=id)
		cv.delete()
		return redirect('user_cv')
	except:
		return redirect('user_cv')

@login_required(login_url='/login/')
def updateusercv(request):
	emp=EmployeeProfile.objects.get(user_id=request.user.id)
	cv=Cv.objects.get(employee_id=emp.id)
	form=CvForm(request.POST or None,instance=cv)
	if form.is_valid():
		form.save()
		return redirect('user_cv')
	context={
		'form':form,
		}
	return render(request,'user_cv.html',context)

def companyvacancyclick(request):
    if request.method=="POST":
        company=CompanyProfile.objects.get(user_id=request.user.id)
        vacancy=Vacancy.objects.filter(Company_id=company.id)
        return render(request,'companyvacancydetail.html')
    else:
        return render(request,'companyvacancydetail.html')



def companyvacancyclickdetails(request,id):
    context = {
    'vacancy':Vacancy.objects.get(pk=id),
    }
    return render(request,'companyvacancydetail.html',context)

def user_existingcv(request,id):
    if request.user.is_authenticated():
        try:
            emp=EmployeeProfile.objects.get(user_id=request.user)
            cv = Cv.objects.filter(employee_id=emp.id)[:1]
            context = {
            'cv':cv,
            'job_id':id,
            }
            return render(request,'existingcv.html',context)
        except:
            comp=CompanyProfile.objects.get(user_id=request.user)
            print("Company cannot apply for this post")
            return render(request,'companycannotapply.html')
    else:
        print("You must log in to apply")
        return redirect('youmustlogin')


def Contact_Us(request):
     return render(request,'Contact_Us.html')


def list_of_applicant(request,id):
	job = Vacancy.objects.get(id=id)
	applicat = Application.objects.filter(vacancy_id=job.id)
	cvid = []
	for x in applicat:
		cvid.append(x.cv_id)
	cv = Cv.objects.filter(id__in=cvid)
	return render (request,'application.html',{'cv':cv})

def cvsave(request):
	if request.user.is_authenticated():
		cv_id = request.POST.get('cvid')
		mycv = Cv.objects.get(id=cv_id)
		job_id = request.POST.get('jobid');
		job = Vacancy.objects.get(id=job_id)
		application = Application(cv_id=mycv.id,vacancy_id=job.id)
		application.save()
		return redirect('Thankyou')
	else:
		return redirect('login')

def Thankyou(request):
	return render(request,'Thankyou.html')

def youmustlogin(request):
	return render(request,'youmustlogin.html')










# @login_required(login_url='/login/')
# def updateusercv(request):
# 	emp=EmployeeProfile.objects.get(user_id=request.user.id)
# 	cv=
# 	form=EmployeeCreateForm(request.POST or None,instance=emp)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('dashboard')
# 	context={
# 		'form':form,
# 		}
# 	return render(request,'updateuser.html',context)
