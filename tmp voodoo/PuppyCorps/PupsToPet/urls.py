from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^dashboard$', views.dashboard, name='dashboard'), # main page
    url(r'^createaccount$', views.createaccount, name='createaccount'),
    url(r'^userinfo$', views.userinfo, name='userinfo'),
    url(r'^createevent$', views.createevent, name='createevent'),
#    url(r'^eventdetail$', views.eventdetail, name='eventdetail') #not made
#    url(r'^login$', views.login, name='login'),
    url(r'^forgotpassword$', views.forgotpassword, name='forgotpassword'),
    url(r'^findevent$', views.findevent, name='findevent'),
    url(r'^doginfo$', views.doginfo, name='doginfo'),
    url(r'^test$', views.test, name='test'),
]
