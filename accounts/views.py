# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from .models import StudentProfile, FacultyProfile
import requests
from django.http import HttpResponse
# from inventory.decorators import student_only, faculty_only


# Create your views here.


class Loginview(View):
    """docstring for Loginview"""

    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(
            'http://yashasingh.tech:8085/api/profiles/login/', data=data)
        data = response.json()
        # print(data['non_field_errors'][0])
        if data.get('non_field_errors') != None:
            return render(request, "accounts/login.html")
        if data.get('group') == "student":
            request.session["id"] = data.get('username')
            request.session["group"] = data.get('group')

            if StudentProfile.objects.filter(
                    username=data.get('username')).count() == 1:
                return redirect('/dashboard')

            else:
                return redirect('/studentprofile')

            return render(request, "accounts/login.html")
        if data.get('group') == "faculty" or data.get('group') == "hod":
            request.session["id"] = data.get('username')
            request.session["group"] = data.get('group')

            if FacultyProfile.objects.filter(
                    username=data.get('username')).count() == 1:
                return redirect('/facultydashboard')

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
        return HttpResponse("succesful")


class Facultyprofileupdate(View):
    # @faculty_only

    def get(self, request):
        return render(request, "accounts/facultyprofile.html")

    def post(self, request):
        # username = request.POST.get('username')
        # branch = request.POST.get('branch')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')
        FacultyProfile.objects.create(username=request.session[
                                      'id'], email=email, phone=Phone)
        return HttpResponse("succesful")


def logoutview(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
