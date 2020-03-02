from django.shortcuts import render
from django.http import HttpResponse


def permission_denied(request, exception=None):
    return render(request, "core/error.html", {'msg': "You are not authorized to access resource", 'res': exception})
