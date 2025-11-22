from django.shortcuts import render, redirect
from .models import *


def driver_list(request):
    drivers = Drivers.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})
