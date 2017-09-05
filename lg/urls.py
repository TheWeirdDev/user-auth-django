from django.conf.urls import url

from . import views

app_name = 'lg'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
