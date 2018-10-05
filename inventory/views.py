from django.shortcuts import render
from .models import departments, inventory
from .models import Issue_list, count_division, storage_location
from accounts.models import StudentProfile, Facultyprofile
from .decorators import student_only, faculty_only
import json


# Create your views here.


@student_only
def StudentDashboard(request):
    # show items
    if request.method == 'GET':
        Branch = departments.objects.filter(
            department=(StudentProfile.objects.get(
                username=request.session['id'])).Branch)
        items = inventory.objects.filter(
            item_department=Branch[0].id)

    return render(request,
                  "inventory/studentdashboarddemo.html",
                  {
                      'data': items
                  }
                  )

    # # Issue request
    if request.method == 'POST':
        # set session['lab'] or sent it via request
        lab = request.session.get('lab')
        faculty = storage_location.object.filter(location=lab).incharge
        student = StudentProfile.objects.filter(username=request.session["id"])
        json_data = json.loads(request.data)
        Issue_list.objects.save(
            item_list=json_data,
            student=student,
            faculty=faculty
        )
    return render(request, "inventory/studentdashboard.html",
                  {'data': items})
    # Issue items
    # if request.method == 'POST':
    #     json_data = json.loads(request.data)
    #     for item in json_data:


@faculty_only
def FacultyDashboard(request):
    """
    Shows the issue requests to the faculty concerned
    """
    if request.method == 'GET':
        profile = Facultyprofile.objects.get(id=request.session['id'])
        data = Issue_list.objects.filter(faculty=profile)
        return render(request,
                      "inventory/facultydashboard.html",
                      {
                          'data': data
                      }
                      )


@faculty_only
def IssueConfirm(request):
    """
    Approve the issue request
    made by the student
    """
    if request.method == "POST":
        # if request['json']:
        json_data = json.loads(request.data)
        # update issue list
        Issue_list.objects.get().update(status=True)
        # update items in the model
        for item in json_data:
            # updates the count of every item in inventry
            count_division.update(item_name=item.id)
    if request.method == 'GET':
        # profile = Facultyprofile.objects.get(id=request.session['id'])
        return render(request, "inventory/facultydashboard.html")
