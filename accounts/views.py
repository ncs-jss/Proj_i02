# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def loginview(request):
	
	return render(request,"accounts/login.html")
