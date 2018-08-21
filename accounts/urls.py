from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Loginview.as_view(), name="login"),
    url(r'^studentprofile$', views.Studentprofileupdate.as_view(),
        name="studentprofile"),
    url(r'^facultyprofile$', views.Facultyprofileupdate.as_view(),
        name="facultyprofile"),
    url(r'^logout/', views.logoutview, name="logout"),
]
