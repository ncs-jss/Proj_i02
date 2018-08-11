from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Loginview.as_view(), name="login"),
    url(r'^logout/', views.logoutview,name="logout"),
]
