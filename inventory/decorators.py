from django.http import HttpResponseRedirect
from django.http import HttpResponse


def student_only(function):
    """Decorator to check if loggedin person is a student """

    def wrap(request, *args, **kwargs):

        group = request.session["group"]
        if group == 'student':
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            # return HttpResponse("wrong user type")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def faculty_only(function):
    """Decorator to check if loggedin person is a faculty """

    def wrap(request, *args, **kwargs):

        group = request.session["group"]
        if group == 'faculty' or group == 'hod':
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
            return HttpResponse("wrong user type")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
