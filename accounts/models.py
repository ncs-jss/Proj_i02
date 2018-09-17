# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
# from django.core.validators import MinValueValidator, MaxValueValidator

# from django.db import models

# Create your models here.

PHONE_VALIDATOR = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Format '+999999999'.Upto 15 digits.")


class StudentProfile(models.Model):
    '''
    It stores information about the Students of college.
    '''

    # List of branches
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'

    BRANCH = (
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (EE, 'Electrical Engineering'),
        (ECE, 'Electronics and Communication Engineering'),
        (EEE, 'Electrical and Electronics Engineering'),
        (CE, 'Civil Engineering'),
        (IC, 'Instrumentation and Control Engineering'),
        (ME, 'Mechanical Engineering'),
    )

    YEAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    username = models.CharField(max_length=60, blank=True, null=True)
    group = models.ForeignKey(Group)
    Branch = models.CharField(
        max_length=5, choices=BRANCH, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(
        validators=[PHONE_VALIDATOR], max_length=15, blank=True)

    created = models.DateTimeField("Created", null=True, auto_now_add=True)

    def __str__(self):
        return self.username


class FacultyProfile(models.Model):
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    BRANCH = (
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (EE, 'Electrical Engineering'),
        (ECE, 'Electronics and Communication Engineering'),
        (EEE, 'Electrical and Electronics Engineering'),
        (CE, 'Civil Engineering'),
        (IC, 'Instrumentation and Control Engineering'),
        (ME, 'Mechanical Engineering'),
    )

    username = models.CharField(max_length=60, blank=True, null=True)
    group = models.ForeignKey(Group, default=1)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(
        validators=[PHONE_VALIDATOR], max_length=15, blank=True, null=True)
    department = models.CharField(
        max_length=15, choices=BRANCH, blank=True, null=True)
    designation = models.CharField(max_length=60, blank=True, null=True)
    created = models.DateTimeField("Created", null=True, auto_now_add=True)

    def __str__(self):
        return self.username
