from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Drivers

# ===================== Проверка авторизации =====================
def is_authenticated(request):
    return request.user.is_authenticated

# ===================== Список водителей с фильтрацией =====================
def driver_list(request):
    drivers = Drivers.objects.all()

    # фильтры через GET-параметры
    name = request.GET.get('name')
    min_rating = request.GET.get('min_rating')
    status = request.GET.get('status')

    if name:
        drivers = drivers.filter(name__icontains=name)
    if min_rating:
        try:
            drivers = drivers.filter(rating__gte=float(min_rating))
        except ValueError:
            pass
    if status in ['active', 'inactive']:
        drivers = drivers.filter(status=(status == 'active'))

    return render(request, 'drivers/drivers_list.html', {'drivers': drivers})

# ===================== Создание водителя =====================
def driver_create(request):
    if not is_authenticated(request):
        return render(request, 'drivers/message.html', {
            'message': "🚫 You must log in to edit a driver."
    })

    if request.method == 'GET':
        return render(request, 'drivers/driver_create.html')
    elif request.method == 'POST':
        driver = Drivers.objects.create(
            name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            car_model=request.POST.get('car_model'),
            car_number=request.POST.get('car_number'),
            rating=request.POST.get('rating'),
            status=request.POST.get('status') == 'on'
        )
        return redirect('driver_detail', driver_id=driver.id)

# ===================== Детали водителя =====================
def driver_detail(request, driver_id):
    driver = Drivers.objects.filter(id=driver_id).first()
    if not driver:
        return HttpResponse('Driver not found')
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

# ===================== Редактирование водителя =====================
def driver_update(request, driver_id):
    if not is_authenticated(request):
        return render(request, 'drivers/message.html', {
            'message': "🚫 You must log in to edit a driver."
    })

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

# ===================== Удаление водителя =====================
def driver_delete_view(request, driver_id):
    if not is_authenticated(request):
        return render(request, 'drivers/message.html', {
            'message': "🚫 You must log in to edit a driver."
    })

    driver = Drivers.objects.filter(id=driver_id).first()
    if not driver:
        return HttpResponse(f"Driver with id {driver_id} not found")

    if request.method == "GET":
        return render(request, "drivers/driver_delete.html", {"driver": driver})
    elif request.method == "POST":
        driver.delete()
        return redirect("driver_list")
