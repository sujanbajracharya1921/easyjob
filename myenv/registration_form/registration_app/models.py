from django.db import models

# Create your models here.
class License(models.Model):
	First_Name=models.CharField(max_length=30)
	Last_Name=models.CharField(max_length=30)
	Address=models.CharField(max_length=30)
	Phone_No=models.CharField(max_length=30 )
	Dob=models.DateField()

	def __str__(self):
		return self.First_Name

 
class Car(models.Model):
	Model=models.CharField(max_length=30)
	Year=models.DateField()
	Color=models.CharField(max_length=30)

	def __str__(self):
		return self.Model 

class Registration(models.Model):
	Register=models.BooleanField()
	License=models.ForeignKey(License)
	Car=models.ForeignKey(Car)

	def __str__(self):
		return str(self.License)



