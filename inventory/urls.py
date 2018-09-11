from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^studentdashboard$', views.StudentDashboard,
        name="dashboard"),
    url(r'^facultydashboard$', views.FacultyDashboard,
        name="facultydashboard"),
]
