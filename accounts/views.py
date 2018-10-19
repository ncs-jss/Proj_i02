from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import StudentProfile, FacultyProfile
import requests
from decouple import config
# from inventory.decorators import student_only, faculty_only


# Create your views here.


class Loginview(View):
    """docstring for Loginview"""

    def get(self, request):
        if request.session.get('id') is not None:
            return redirect('/dashboard/studentdashboard')
        return render(request, "accounts/login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(
            config('LOGIN_API'),
            data=data)
        data = response.json()
        if data.get('non_field_errors') is not None:
            return render(request, "accounts/login.html")
        if data.get('group') == "student":
            request.session["id"] = data.get('username')
            request.session["group"] = data.get('group')
            if StudentProfile.objects.filter(
                    username=data.get('username')).count() == 1:
                return redirect('/dashboard/studentdashboard')
            else:
                return redirect('/studentprofile')
            return render(request, "accounts/login.html")
        if data.get('group') == "faculty" or data.get('group') == "hod":
            request.session["id"] = data.get('username')
            request.session["group"] = data.get('group')
            if FacultyProfile.objects.filter(
                    username=data.get('username')).count() == 1:
                return redirect('dashboard/facultydashboard')
            else:
                return redirect('/facultyprofile')
            # print("Faculty login")
        # if data.get('group') == "hod":
        #     request.session["id"] = data.get('username')
        #     request.session["group"] = data.get('group')

        #     # render (account/studentprofile.html)
        #     print("HOD login")


class Studentprofileupdate(View):
    # @student_only

    def get(self, request):
        if StudentProfile.objects.filter(
                username=request.session['id']).count() == 1:
            return redirect('/dashboard/studentdashboard')
        return render(request, "accounts/studentprofile.html")

    def post(self, request):
        # username = request.POST.get('username')
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')
        StudentProfile.objects.create(
            username=request.session['id'],
            group=branch, Branch=branch,
            email=email, phone=Phone)
        # return HttpResponse("succesful")
        return redirect('/dashboard')


class Facultyprofileupdate(View):
    # @faculty_only

    def get(self, request):
        if FacultyProfile.objects.filter(
                username=request.session[id]).count() == 1:
            return redirect('/facultydashboard')
        return render(request, "accounts/facultyprofile.html")

    def post(self, request):
        # username = request.POST.get('username')
        # branch = request.POST.get('branch')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')
        FacultyProfile.objects.create(username=request.session[
                                      'id'], email=email, phone=Phone)
        # return HttpResponse("succesful")
        return redirect('/dashboard')


def logoutview(request):
    try:
        del request.session['id']
        del request.session['group']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
