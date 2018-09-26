from django.db import models
from django.contrib.auth.models import User
from employee.models import Cv
from ckeditor.fields import RichTextField

# Create your models here.


class CompanyProfile(models.Model):
	company_name=models.CharField(max_length=30,unique=True)
	address=models.CharField(max_length=30)
	contact_no=models.CharField(max_length=10,unique=True)
	portfolio=models.URLField(null=True,unique=True)
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.company_name

class Vacancy(models.Model):
	title=models.CharField(max_length=30)
	description=RichTextField(blank=False)
	tag=models.CharField(max_length=100,blank=False)
	vacancy_location=models.CharField(max_length=30,null=True)
	company=models.ForeignKey(CompanyProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Application(models.Model):
	cv=models.ForeignKey(Cv,on_delete=models.CASCADE)
	vacancy=models.ForeignKey(Vacancy,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.vacancy)
