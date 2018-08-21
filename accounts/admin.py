# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentProfile, FacultyProfile

# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(FacultyProfile)
