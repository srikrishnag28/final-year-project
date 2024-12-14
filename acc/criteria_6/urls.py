from django.urls import path
from .views import *

urlpatterns = [
    path('6_1_1/form/', criteria_6_1_1_form, name='criteria_6_1_1_form'),
    path('6_1_1/', criteria_6_1_1, name='criteria_6_1_1'),
    path('6_1_1/delete', criteria_6_1_1_delete, name='criteria_6_1_1_delete'),
    
    path('6_2_1/form/', criteria_6_2_1_form, name='criteria_6_2_1_form'),
    path('6_2_1/', criteria_6_2_1, name='criteria_6_2_1'),
    path('6_2_1/delete', criteria_6_2_1_delete, name='criteria_6_2_1_delete'),

    path('6_2_2/', criteria_6_2_2, name='criteria_6_2_2'),

    path('6_3_1/form/', criteria_6_3_1_form, name='criteria_6_3_1_form'),
    path('6_3_1/', criteria_6_3_1, name='criteria_6_3_1'),
    path('6_3_1/delete', criteria_6_3_1_delete, name='criteria_6_3_1_delete'),
    
    path('6_3_2/', criteria_6_3_2, name='criteria_6_3_2'),
    path('6_3_2/form/', criteria_6_3_2_form, name='criteria_6_3_2_form'),
    path('6_3_2/upload_excel/', upload_excel_6_3_2, name='upload_excel_6_3_2'),
    path('6_3_2/export_excel/', export_excel_6_3_2, name='export_excel_6_3_2'),

    path('6_3_3/', criteria_6_3_3, name='criteria_6_3_3'),
    path('6_3_3/form/', criteria_6_3_3_form, name='criteria_6_3_3_form'),
    path('6_3_3/upload_excel/', upload_excel_6_3_3, name='upload_excel_6_3_3'),
    path('6_3_3/export_excel/', export_excel_6_3_3, name='export_excel_6_3_3'),
    
    path('6_4_1/form/', criteria_6_4_1_form, name='criteria_6_4_1_form'),
    path('6_4_1/', criteria_6_4_1, name='criteria_6_4_1'),
    path('6_4_1/delete', criteria_6_4_1_delete, name='criteria_6_4_1_delete'),
    
    path('6_5_1/form/', criteria_6_5_1_form, name='criteria_6_5_1_form'),
    path('6_5_1/', criteria_6_5_1, name='criteria_6_5_1'),
    path('6_5_1/delete', criteria_6_5_1_delete, name='criteria_6_5_1_delete'),

    path('6_5_2/', criteria_6_5_2, name='criteria_6_5_2'),
]