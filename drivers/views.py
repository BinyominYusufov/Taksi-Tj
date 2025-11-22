from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def driver_list(request):
    drivers = Drivers.objects.all()
    return render(request, 'drivers/drivers_list.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = Drivers.objects.get(id=driver_id)
    if not driver:
        return HttpResponse('Driver not found')
    return render(request, 'drivers/driver_detail.html', {'driver': driver})
