from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeProfile(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	portfolio=models.URLField(null=True,unique=True)
	contact=models.CharField(max_length=10,unique=True)
	user=models.OneToOneField(User)

	def __str__(self):
		return self.name


class Skill(models.Model):
	skill=models.CharField(unique=False,max_length=30)
	employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.skill

class Training(models.Model):
	training_name=models.CharField(max_length=30)
	institute=models.CharField(max_length=30)
	employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.training_name

class Experience(models.Model):
	company=models.CharField(max_length=30)
	start_date=models.DateField()
	end_date=models.DateField(blank=True)
	employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.company

class Degree(models.Model):
	degree_name=models.CharField(max_length=30)
	institution=models.CharField(max_length=30)
	employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.degree_name

class Cv(models.Model):
	name=models.CharField(max_length=30)
	cv_file=models.FileField(upload_to='cv/')
	image = models.ImageField(upload_to='image/',blank=True)
	employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
