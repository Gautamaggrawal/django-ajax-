from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^userdetails/$', views.ProfileDetails.as_view(), name='userdetails'),
    url(r'^login/$', views.LoginUserView.as_view(), name='login'),
    url(r'^signup/$', views.SignupUserView.as_view(), name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
]

