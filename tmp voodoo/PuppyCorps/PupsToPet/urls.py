from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^createaccount$', views.createaccount, name='createaccount'),
    url(r'^login$', views.login, name='login'),
    url(r'^forgotpassword$', views.forgotpassword, name='forgotpassword'),
    url(r'^createevent$', views.createevent, name='createevent'),
    url(r'^findevent$', views.findevent, name='findevent'),
    url(r'^userinfo$', views.userinfo, name='userinfo'),
    url(r'^doginfo$', views.doginfo, name='doginfo'),
    url(r'^vomit$', views.vomit, name='vomit'),
]