from django.conf.urls import include, url
from .import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.social),
    url(r'^1/$',views.social1),
    ]