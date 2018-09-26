from django.conf.urls import include, url
from .import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.company),
    url(r'^vacancy/',views.vacancy,name='vacancy'),
    url(r'^1/$',views.company1),
    url(r'^1/2/$',views.company2)
    ]
