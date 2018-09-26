from django.conf.urls import include, url
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index,name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^company/',include('company.urls')),
    url(r'^employee/',include('employee.urls')),
    url(r'^social/',include('social.urls')),
    url(r'^search/$',views.search,name='search'),

    # url(r'^blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
