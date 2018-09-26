from django.conf.urls import include, url
from .import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.employee),
    url(r'^1/$',views.employee1),
    url(r'^1/2/$',views.employee2)
    ]