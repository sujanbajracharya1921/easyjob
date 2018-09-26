from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.CompanyProfile)
admin.site.register(models.Vacancy)
admin.site.register(models.Application)
