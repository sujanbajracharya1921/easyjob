from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategory(models.Model):
	category=models.CharField(max_length=30)

	def __str__(self):
		return self.category

class Blog(models.Model):
	title=models.CharField(max_length=30)
	content=RichTextField()
	image=models.ImageField(upload_to='image/')
	tag=models.CharField(max_length=30)
	category=models.ForeignKey(BlogCategory,on_delete=models.CASCADE)

	def __str__(self):
		return self.title