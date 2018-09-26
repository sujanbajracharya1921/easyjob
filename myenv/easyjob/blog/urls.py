from django.conf.urls import include, url
from .import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.blog,name='blog'),
 	url('^(?P<id>[0-9]+)/$',views.blog_details,name='blog_details')
    ]