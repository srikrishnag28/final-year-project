from django.urls import path
from .views import *

urlpatterns = [
    path('3_1_1/', criteria_3_1_1, name='criteria_3_1_1'),
    path('3_1_1/form/', criteria_3_1_1_form, name='criteria_3_1_1_form'),
    path('3_1_1/upload_excel/', upload_excel_3_1_1, name='upload_excel_3_1_1'),
    path('3_1_1/export_excel/', export_excel_3_1_1, name='export_excel_3_1_1'),

    path('3_2_1/form/', criteria_3_2_1_form, name='criteria_3_2_1_form'),
    path('3_2_1/', criteria_3_2_1, name='criteria_3_2_1'),
    path('3_2_1/delete', criteria_3_2_1_delete, name='criteria_3_2_1_delete'),

    path('3_2_2/', criteria_3_2_2, name='criteria_3_2_2'),
    path('3_2_2/form/', criteria_3_2_2_form, name='criteria_3_2_2_form'),
    path('3_2_2/upload_excel/', upload_excel_3_2_2, name='upload_excel_3_2_2'),
    path('3_2_2/export_excel/', export_excel_3_2_2, name='export_excel_3_2_2'),

    path('3_3_1/', criteria_3_3_1, name='criteria_3_3_1'),
    path('3_3_1/form/', criteria_3_3_1_form, name='criteria_3_3_1_form'),
    path('3_3_1/upload_excel/', upload_excel_3_3_1, name='upload_excel_3_3_1'),
    path('3_3_1/export_excel/', export_excel_3_3_1, name='export_excel_3_3_1'),
        
    path('3_3_2/', criteria_3_3_2, name='criteria_3_3_2'),
    path('3_3_2/form/', criteria_3_3_2_form, name='criteria_3_3_2_form'),
    path('3_3_2/upload_excel/', upload_excel_3_3_2, name='upload_excel_3_3_2'),
    path('3_3_2/export_excel/', export_excel_3_3_2, name='export_excel_3_3_2'),

    path('3_4_1/form/', criteria_3_4_1_form, name='criteria_3_4_1_form'),
    path('3_4_1/', criteria_3_4_1, name='criteria_3_4_1'),
    path('3_4_1/delete', criteria_3_4_1_delete, name='criteria_3_4_1_delete'),
    
    path('3_4_2/form/', criteria_3_4_2_form, name='criteria_3_4_2_form'),
    path('3_4_2/', criteria_3_4_2, name='criteria_3_4_2'),
    path('3_4_2/delete', criteria_3_4_2_delete, name='criteria_3_4_2_delete'),
    
    path('3_4_3/', criteria_3_4_3, name='criteria_3_4_3'),
    path('3_4_3/form/', criteria_3_4_3_form, name='criteria_3_4_3_form'),
    path('3_4_3/upload_excel/', upload_excel_3_4_3, name='upload_excel_3_4_3'),
    path('3_4_3/export_excel/', export_excel_3_4_3, name='export_excel_3_4_3'),

    path('3_5_1/', criteria_3_5_1, name='criteria_3_5_1'),
    path('3_5_1/form/', criteria_3_5_1_form, name='criteria_3_5_1_form'),
    path('3_5_1/upload_excel/', upload_excel_3_5_1, name='upload_excel_3_5_1'),
    path('3_5_1/export_excel/', export_excel_3_5_1, name='export_excel_3_5_1'),
]