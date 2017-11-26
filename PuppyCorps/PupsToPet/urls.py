from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^dashboard$', views.dashboard, name='dashboard'), # main page
    url(r'^createaccount$', views.createaccount, name='createaccount'),
    url(r'^userinfo$', views.userinfo, name='userinfo'),
    url(r'^createevent$', views.createevent, name='createevent'),
#    url(r'^eventdetail$', views.eventdetail, name='eventdetail') #not made
    url(r'^login$', views.login, name='login'),
    url(r'^loggedout$', views.loggedout, name='loggedout'),
#    url(r'^forgotpassword$', views.forgotpassword, name='forgotpassword'),
    url(r'^findevent$', views.findevent, name='findevent'),
    url(r'^doginfo$', views.doginfo, name='doginfo'),
               # the following below might not be necessary.
               #    Depends on if we want to do password reset for our app
    url(r'^passwordresetform$', views.passwordresetform, name='passwordresetform'),
    url(r'^passwordresetdone$', views.passwordresetdone, name='passwordresetdone'),
    url(r'^passwordresetemail$', views.passwordresetemail, name='passwordresetemail'),
    url(r'^passwordresetconfirm$', views.passwordresetconfirm, name='passwordresetconfirm'),
    url(r'^passwordresetcomplete$', views.passwordresetcomplete, name='passwordresetcomplete'),

]
