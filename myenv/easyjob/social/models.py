from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SocialLink(models.Model):
	facebook=models.URLField()
	instagram=models.URLField()
	linkedin=models.URLField()
	twitter=models.URLField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.facebook