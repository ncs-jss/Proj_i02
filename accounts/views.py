# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from .models import *
import requests
from django.shortcuts import redirect


# Create your views here.


class Loginview(View):
    """docstring for Loginview"""

    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        print("enter login post")
        username = request.POST['username']
        password = request.POST['password']
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(
            'http://yashasingh.tech:8085/api/profiles/login/', data=data)
        print(response.json())
        data = response.json()
        # print(data['non_field_errors'][0])
        if data.get('non_field_errors') != None:
            print("Incorrect credentials")
            return render(request, "accounts/login.html")
        if data.get('group') == "student":
            print("student login")
            request.session["id"] = data.get('username')
            if StudentProfile.objects.filter(username=data.get('username')).count() == 1:
                print("already there")
                return redirect('/dashboard')

            else:
                print("New student")
                return redirect('/studentprofile')

            return render(request, "accounts/login.html")
        if data.get('group') == "faculty":
            print("student login")
            request.session["id"] = data.get('username')
            if FacultyProfile.objects.filter(username=data.get('username')).count() == 1:
                print("already there")
                return redirect('/dashboard')

            else:
                print("New student")
                return redirect('/facultyprofile')
            print("Faculty login")
        if data.get('group') == "hod":
            request.session["id"] = data.get('username')
            # render (account/studentprofile.html)
            print("HOD login")


class Studentprofileupdate(View):

    def get(self, request):
        return render(request, "accounts/studentprofile.html")

    def post(self, request):
        print("enter student post")
        username = request.POST.get('username')
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        Phoneno = request.POST.get('phoneno')
        StudentProfile.objects.create(username=request.session[
                                      'id'], branch=branch, email=email, phoneno=phoneno)


class Facultyprofileupdate(View):

    def get(self, request):
        return render(request, "accounts/facultyprofile.html")


def logoutview():
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def Dashboard(request):
    return render(request, "inventory/studentdashboard.html")
