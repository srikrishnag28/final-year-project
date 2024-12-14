from django.urls import path
from .views import *

urlpatterns = [
    path('5_1_1/', criteria_5_1_1, name='criteria_5_1_1'),
    path('5_1_1/form/', criteria_5_1_1_form, name='criteria_5_1_1_form'),
    path('5_1_1/upload_excel/', upload_excel_5_1_1, name='upload_excel_5_1_1'),
    path('5_1_1/export_excel/', export_excel_5_1_1, name='export_excel_5_1_1'),

    path('5_1_2/', criteria_5_1_2, name='criteria_5_1_2'),

    path('5_1_3/', criteria_5_1_3, name='criteria_5_1_3'),
    path('5_1_3/form/', criteria_5_1_3_form, name='criteria_5_1_3_form'),
    path('5_1_3/upload_excel/', upload_excel_5_1_3, name='upload_excel_5_1_3'),
    path('5_1_3/export_excel/', export_excel_5_1_3, name='export_excel_5_1_3'),

    path('5_1_4/', criteria_5_1_4, name='criteria_5_1_4'),

    path('5_2_1/', criteria_5_2_1, name='criteria_5_2_1'),
    path('5_2_1/5_2_1_1/form/', criteria_5_2_1_1_form, name='criteria_5_2_1_1_form'),
    path('5_2_1/5_2_1_2/form/', criteria_5_2_1_2_form, name='criteria_5_2_1_2_form'),
    path('5_2_1/5_2_1_1/upload_excel/', upload_excel_5_2_1_1, name='upload_excel_5_2_1_1'),
    path('5_2_1/5_2_1_2/upload_excel/', upload_excel_5_2_1_2, name='upload_excel_5_2_1_2'),
    path('5_2_1/export_excel/', export_excel_5_2_1, name='export_excel_5_2_1'),

    path('5_2_2/', criteria_5_2_2, name='criteria_5_2_2'),
    path('5_2_2/form/', criteria_5_2_2_form, name='criteria_5_2_2_form'),
    path('5_2_2/upload_excel/', upload_excel_5_2_2, name='upload_excel_5_2_2'),
    path('5_2_2/export_excel/', export_excel_5_2_2, name='export_excel_5_2_2'),
    
    path('5_3_1/', criteria_5_3_1, name='criteria_5_3_1'),
    path('5_3_1/form/', criteria_5_3_1_form, name='criteria_5_3_1_form'),
    path('5_3_1/upload_excel/', upload_excel_5_3_1, name='upload_excel_5_3_1'),
    path('5_3_1/export_excel/', export_excel_5_3_1, name='export_excel_5_3_1'),
    
    path('5_3_2/', criteria_5_3_2, name='criteria_5_3_2'),
    path('5_3_2/form/', criteria_5_3_2_form, name='criteria_5_3_2_form'),
    path('5_3_2/upload_excel/', upload_excel_5_3_2, name='upload_excel_5_3_2'),
    path('5_3_2/export_excel/', export_excel_5_3_2, name='export_excel_5_3_2'),
    
    path('5_4_1/form/', criteria_5_4_1_form, name='criteria_5_4_1_form'),
    path('5_4_1/', criteria_5_4_1, name='criteria_5_4_1'),
    path('5_4_1/delete', criteria_5_4_1_delete, name='criteria_5_4_1_delete'),
]