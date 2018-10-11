from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import StudentProfile, FacultyProfile
import jsonfield


# Create your models here.
class departments(models.Model):
    '''
    It stores the information about the Department
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

    department = models.CharField(max_length=10, choices=BRANCH)

    class Meta:
        verbose_name = _("Department")

    def __str__(self):
        return self.department


class storage_locations(models.Model):
    location = models.CharField(max_length=30)
    department = models.ForeignKey(departments, on_delete=models.CASCADE)
    incharge = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Location")

    def __str__(self):
        return self.location


class inventory(models.Model):
    item = models.CharField(max_length=50)
    item_total_count = models.IntegerField(default=0)
    item_department = models.ForeignKey(departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class count_division(models.Model):
    item_name = models.ForeignKey(inventory, on_delete=models.CASCADE)
    location = models.ForeignKey(storage_locations, on_delete=models.CASCADE)
    item_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("DividedCount")

    def __str__(self):
        return self.item_name


class Issue_list(models.Model):
    item_list = jsonfield.JSONField()
    status = models.BooleanField(default=False)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("IssueList")

    def __str__(self):
        return self.item_list
