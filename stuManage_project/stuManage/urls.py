from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^students/$', views.students),

    url(r'^showverify/$', views.showverify, name='showverify'),
    url(r'^login/$', views.login, name='login'),
    url(r'^verifyvalidate/$', views.verifyvalidate, name='verifyvalidate'),
    url(r'^userLogin/$', views.userLogin, name='userLogin'),
    url(r'^uerLogout/$', views.uerLogout, name='uerLogout'),

    url(r'^index/$', views.index, name='index'),

    url(r'^students/(\d+)/$', views.students, name='students'),
    url(r'^stuList/(\d+)/$', views.stuList, name='stuList'),

    url(r'^editstu/(\d+)/$', views.editstu, name='editstu'),
    url(r'^addstu/', views.addstu, name='addstu'),
    url(r'^addOrEditStu/$', views.addOrEditStu, name='addOrEditStu'),
    url(r'^importstu/$', views.importstu, name='importstu'),
    url(r'^importStu/$', views.importStu, name='importStu'),



    url(r'^testAJAX/', views.testAJAX, name='testAJAX'),
    url(r'^TestAJAX/', views.TestAJAX, name='TestAJAX'),
    url(r'^testValidate/', views.testValidate, name='testValidate'),
]