# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

PHONE_VALIDATOR = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class StudentProfile(models.Model):
    username = models.CharField(max_length=60, blank=True, null=True)
    group = models.CharField(max_length=60, blank=True, null=True)
    Branch = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(
        validators=[PHONE_VALIDATOR], max_length=15, blank=True)


class FacultyProfile(models.Model):
    username = models.CharField(max_length=60, blank=True, null=True)
    group = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(
        validators=[PHONE_VALIDATOR], max_length=15, blank=True)
    department = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=60, blank=True, null=True)
