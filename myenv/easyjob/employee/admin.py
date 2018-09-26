from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.EmployeeProfile)
admin.site.register(models.Skill)
admin.site.register(models.Training)
admin.site.register(models.Experience)
admin.site.register(models.Degree)
admin.site.register(models.Cv)