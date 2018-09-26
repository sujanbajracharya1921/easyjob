from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.BlogCategory)
admin.site.register(models.Blog)