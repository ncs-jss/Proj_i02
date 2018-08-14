from django.shortcuts import render
from .models import *
from accounts.models import *
from .models import *

# Create your views here.


class StudentDashboard():

    def get(self, request):
        profile = Studentprofile.objects.get(
            id=request.session['id'])
        items = inventory.objects.filter(
            item_department__iexact=profile.department)
        return render(request, "inventry/studentdashboard.html")

    def post(self, request):
        # pass


class FacultyDashboard():

    def get(self, request):
        profile = Facultyprofile.objects.get(id=request.session['id'])
        return render(request, "inventry/Facultydashboard.html")

    def post(self, request):
        pass


# class itemissue():


# class issuepermission():
