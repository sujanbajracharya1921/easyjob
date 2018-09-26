from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/',views.blog),
    url(r'^index/',views.index),
    url(r'^admin/', include(admin.site.urls)),
]
