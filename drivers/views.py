from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def driver_list(request):
    drivers = Drivers.objects.all()
    return render(request, 'drivers/drivers_list.html', {'drivers': drivers})

def driver_create(request):
    if request.method == 'GET':
        return render(request, 'drivers/driver_create.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        car_model = request.POST.get('car_model')
        car_number = request.POST.get('car_number')
        rating = request.POST.get('rating')
        status = request.POST.get('status') == 'on'
        driver = Drivers.objects.create(
            name=name,
            phone_number=phone_number,
            car_model=car_model,
            car_number=car_number,
            rating=rating,
            status=status
        )
        return redirect('driver_detail', driver_id=driver.id)

def driver_detail(request, driver_id):
    driver = Drivers.objects.get(id=driver_id)
    if not driver:
        return HttpResponse('Driver not found')
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

def driver_update(request, driver_id):
    driver = Drivers.objects.filter(id=driver_id).first()
    if not driver:
        return HttpResponse('Driver not found')
    if request.method == 'GET':
        return render(request, 'drivers/driver_update.html', {'driver': driver})
    elif request.method == 'POST':
        driver.name = request.POST.get('name')
        driver.phone_number = request.POST.get('phone_number')
        driver.car_model = request.POST.get('car_model')
        driver.car_number = request.POST.get('car_number')
        driver.rating = request.POST.get('rating')
        driver.status = request.POST.get('status') == 'on'
        driver.save()
        return redirect('driver_detail', driver_id=driver.id)
    
def driver_delete_view(request, driver_id):
    driver = Drivers.objects.filter(id=driver_id).first()
    if not driver:
        return HttpResponse(f"Driver with id {driver_id} not found")
    if request.method == "GET":
        return render(request, "drivers/driver_delete.html", context={"driver":driver})
    elif request.method == "POST":
        driver.delete()
        return redirect("driver_list")

    

    