from django.db import models

# Create your models here.
class CategoryTable(models.Model):
	category_name=models.CharField(max_length=30)

	def __str__(self):
		return self.category_name

class Blog(models.Model):
	title=models.CharField(max_length=30)
	description=models.TextField()
	category_id=models.ForeignKey(CategoryTable)

	def __str__(self):
		return self.title