from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views
from accounts.forms import LoginForm



urlpatterns =[
    url(r'^login/$', login, kwargs = {'authentication_form' : LoginForm, }),
    url(r'^profile/(?P<pk>\d+)$', views.profile),
    url(r'^signup/$', views.signup),
    url(r'^logout/$', views.logout),

]
