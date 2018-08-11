# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
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
                return redirect('######')

            else:
                print("New student")
                return redirect('Studentprofileupdate')

            return render(request, "accounts/login.html")
        if data.get('group') == "faculty":
            print("student login")
            request.session["id"] = data.get('username')
            if FacultyProfile.objects.filter(username=data.get('username')).count() == 1:
                print("already there")
                return redirect('######')

            else:
                print("New student")
                return redirect('Facultyprofileupdate')
            print("Faculty login")
        if data.get('group') == "hod":
        	request.session["id"] = data.get('username')
            # render (account/studentprofile.html)
            print("HOD login")


def Studentprofileupdate():
    username = request.POST['username']
    password = request.POST['password']


def Facultyprofileupdate():
    username = request.POST['username']
    password = request.POST['password']


def logoutview():
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
