from django.shortcuts import render
from .models import departments, inventory
from accounts.models import StudentProfile
from .decorators import student_only, faculty_only
# import json

# Create your views here.


# def itemissue(request):


@student_only
def StudentDashboard(request):
    # show items
    if request.method == 'GET':
        Branch = departments.objects.filter(
            department=(StudentProfile.objects.get(
                username=request.session['id'])).Branch)
        items = inventory.objects.filter(
            item_department=Branch[0].id)
        return render(request, "inventory/studentdashboard.html")
    # Issue items
    # if request.method == 'POST':
    #     json_data = json.loads(request.data)
    #     for item in json_data:


@faculty_only
def FacultyDashboard(request):
    if request.method == 'GET':
        # profile = Facultyprofile.objects.get(id=request.session['id'])
        return render(request, "inventory/facultydashboard.html")
