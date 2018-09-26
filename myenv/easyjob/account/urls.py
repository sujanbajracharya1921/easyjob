from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'easyjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^profile/',views.headerprofile,name='headerprofile'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/account/login'},name='logout'),
    url(r'^dashboard/', views.dashboard,name='dashboard'),
    url(r'^whoareyou/', views.whoareyou,name='whoareyou'),
    url(r'^employeeaccount/', views.employeeaccount,name='employeeaccount'),
    url(r'^employeeskill/', views.employeeskill,name='employeeskill'),
    url(r'^employeetraining/', views.employeetraining,name='employeetraining'),
    url(r'^employeeexperience/', views.employeeexperience,name='employeeexperience'),
    url(r'^employeedegree/', views.employeedegree,name='employeedegree'),
    url(r'^employeecv/(?P<id>[0-9]+)$',views.user_existingcv,name='user_existingcv'),
    url(r'^employeecv/', views.employeecv,name='employeecv'),
    url(r'^companyaccount/', views.companyaccount,name='companyaccount'),
    url(r'^addvacancy/$', views.addvacancy,name='addvacancy'),
    url(r'^allvacancy/$', views.allvacancy,name='allvacancy'),
    url(r'^dashboards/', views.dashboards,name='dashboards'),
    url(r'^allvacancy/(?P<id>[0-9]+)/readmore/$', views.readmore,name='readmore'),
    url(r'^allvacancy/(?P<id>[0-9]+)/update/$', views.updatevacancy,name='updatevacancy'),
    url(r'^allvacancy/(?P<id>[0-9]+)/delete/$', views.deletevacancy,name='deletevacancy'),
    url(r'^user_update/$', views.updateuser,name='updateuser'),
    url(r'^user_update_skill/$', views.updateuserskill,name='updateuserskill'),
    url(r'^user_update_skill/(?P<id>[0-9]+)/delete/$', views.deleteuserskill,name='deleteuserskill'),
    url(r'^user_cv/$', views.user_cv,name='user_cv'),
    url(r'^user_cv/(?P<id>[0-9]+)/deleteusercv/$', views.deleteusercv,name='deleteusercv'),
    url(r'^updateusercv/$', views.updateusercv,name='updateusercv'),
    url(r'^companyvacancyclick/$',views.companyvacancyclick,name='companyvacancyclick'),
    url(r'^companyvacancyclick/(?P<id>[0-9]+)/$',views.companyvacancyclickdetails,name='companyvacancyclickdetails'),
    url(r'^Contact_Us/',views.Contact_Us,name='Contact_Us'),
    url(r'^list_of_applicant/(?P<id>[0-9]+)/$',views.list_of_applicant,name='list_of_applicant'),
    url(r'^cvsave/',views.cvsave,name='cvsave'),
    url(r'^Thankyou/',views.Thankyou,name='Thankyou'),
    url(r'^youmustlogin/',views.youmustlogin,name='youmustlogin'),
    url(r'^updatecompany/',views.updatecompany,name='updatecompany'),







]
