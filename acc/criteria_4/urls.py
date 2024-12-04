from django.urls import path
from .views import *

urlpatterns = [
    path('4_1_1/form/', criteria_4_1_1_form, name='criteria_4_1_1_form'),
    path('4_1_1/', criteria_4_1_1, name='criteria_4_1_1'),
]