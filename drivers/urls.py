from django.urls import path
from .views import *


urlpatterns = [
    path('', driver_list, name='driver_list'),
    path('<int:driver_id>/', driver_detail, name='driver_detail'),
]