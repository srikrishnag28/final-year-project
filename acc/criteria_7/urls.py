from django.urls import path
from .views import *

urlpatterns = [
    path('7_1_1/form/', criteria_7_1_1_form, name='criteria_7_1_1_form'),
    path('7_1_1/', criteria_7_1_1, name='criteria_7_1_1'),
    path('7_1_1/delete', criteria_7_1_1_delete, name='criteria_7_1_1_delete'),

    path('7_1_2/', criteria_7_1_2, name='criteria_7_1_2'),

    path('7_1_3/', criteria_7_1_3, name='criteria_7_1_3'),

    path('7_1_4/form/', criteria_7_1_4_form, name='criteria_7_1_4_form'),
    path('7_1_4/', criteria_7_1_4, name='criteria_7_1_4'),
    path('7_1_4/delete', criteria_7_1_4_delete, name='criteria_7_1_4_delete'),
    
    path('7_2_1/form/', criteria_7_2_1_form, name='criteria_7_2_1_form'),
    path('7_2_1/', criteria_7_2_1, name='criteria_7_2_1'),
    path('7_2_1/delete', criteria_7_2_1_delete, name='criteria_7_2_1_delete'),
    
    path('7_3_1/form/', criteria_7_3_1_form, name='criteria_7_3_1_form'),
    path('7_3_1/', criteria_7_3_1, name='criteria_7_3_1'),
    path('7_3_1/delete', criteria_7_3_1_delete, name='criteria_7_3_1_delete'),
]