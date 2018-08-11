from django.shortcuts import render
from .models import *
from accounts.models import *
from .models import *

# Create your views here.


class StudentDashboard():

    def get(self, request):
        profile = Studentprofile.objects.get(
            id=request.session['id'])
        items = inventry.objects.filter(Department_iexact=profile.department)
        return render(request, "inventry/studentdashboard.html")

    def post(self, request):


class FacultyDashboard():

    def get(self, request):
    	profile = Facultyprofile.objects.get(
            id=request.session['id'])
        return render(request, "inventry/Facultydashboard.html")

    def post(self, request):
