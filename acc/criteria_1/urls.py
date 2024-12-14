from django.urls import path
from .views import *

urlpatterns = [
    path('1_1_1/form/', criteria_1_1_1_form, name='criteria_1_1_1_form'),
    path('1_1_1/', criteria_1_1_1, name='criteria_1_1_1'),
    path('1_1_1/delete', criteria_1_1_1_delete, name='criteria_1_1_1_delete'),

    path('1_2_1/', criteria_1_2_2, name='criteria_1_2_2'),
    path('1_2_1/form/', criteria_1_2_2_form, name='criteria_1_2_2_form'),
    path('1_2_1/upload_excel/', upload_excel_1_2_2, name='upload_excel_1_2_2'),
    path('1_2_1/export_excel/', export_excel_1_2_2, name='export_excel_1_2_2'),

    path('1_2_2/', criteria_1_2_2, name='criteria_1_2_2'),
    path('1_2_2/form/', criteria_1_2_2_form, name='criteria_1_2_2_form'),
    path('1_2_2/upload_excel/', upload_excel_1_2_2, name='upload_excel_1_2_2'),
    path('1_2_2/export_excel/', export_excel_1_2_2, name='export_excel_1_2_2'),
    
    path('1_3_1/form/', criteria_1_3_1_form, name='criteria_1_3_1_form'),
    path('1_3_1/', criteria_1_3_1, name='criteria_1_3_1'),
    path('1_3_1/delete', criteria_1_3_1_delete, name='criteria_1_3_1_delete'),
    
    path('1_3_2/', criteria_1_3_2, name='criteria_1_3_2'),
    path('1_3_2/form/', criteria_1_3_2_form, name='criteria_1_3_2_form'),
    path('1_3_2/upload_excel/', upload_excel_1_3_2, name='upload_excel_1_3_2'),
    path('1_3_2/export_excel/', export_excel_1_3_2, name='export_excel_1_3_2'),
]