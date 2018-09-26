from django.db import models

# Create your models here.
class Category(models.Model):
	category_name=models.CharField(max_length=30)

	def __str__(self):
		return self.category_name

class JobVacancy(models.Model):
	title=models.CharField(max_length=30)
	description=models.TextField()
	skill=models.CharField(max_length=30)
	category_id=models.ForeignKey(Category)

	def __str__(self):
		return self.title
		