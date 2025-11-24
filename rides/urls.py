from django.urls import path
<<<<<<< HEAD


urlpatterns = [
    
=======
from .views import *

urlpatterns = [
    path("", ride_list, name="ride_list"),
    path("create/", ride_create, name="ride_create"),
    path("<int:ride_id>/", ride_detail, name="ride_detail"),
    path("<int:ride_id>/update/", ride_update, name="ride_update"),
    path("<int:ride_id>/delete/", ride_delete, name="ride_delete"),
>>>>>>> e05827da18bb32d36262b0d5d332ba8484db5ad4
]
