from django.urls import path
from .views import *

urlpatterns = [
    
    path('2_3_1/form/', criteria_2_3_1_form, name='criteria_2_3_1_form'),
    path('2_3_1/', criteria_2_3_1, name='criteria_2_3_1'),
    path('2_3_1/delete', criteria_2_3_1_delete, name='criteria_2_3_1_delete'),

    path('2_4_2/', criteria_2_4_2, name='criteria_2_4_2'),
    path('2_4_2/2_4_2_1/form/', criteria_2_4_2_1_form, name='criteria_2_4_2_1_form'),
    path('2_4_2/2_4_2_2/form/', criteria_2_4_2_2_form, name='criteria_2_4_2_2_form'),
    path('2_4_2/2_4_2_1/upload_excel/', upload_excel_2_4_2_1, name='upload_excel_2_4_2_1'),
    path('2_4_2/2_4_2_2/upload_excel/', upload_excel_2_4_2_2, name='upload_excel_2_4_2_2'),
    path('2_4_2/export_excel/', export_excel_2_4_2, name='export_excel_2_4_2'),
    
    path('2_5_1/form/', criteria_2_5_1_form, name='criteria_2_5_1_form'),
    path('2_5_1/', criteria_2_5_1, name='criteria_2_5_1'),
    path('2_5_1/delete', criteria_2_5_1_delete, name='criteria_2_5_1_delete'),

    path('2_6_1/form/', criteria_2_6_1_form, name='criteria_2_6_1_form'),
    path('2_6_1/', criteria_2_6_1, name='criteria_2_6_1'),
    path('2_6_1/delete', criteria_2_6_1_delete, name='criteria_2_6_1_delete'),

    path('2_6_2/form/', criteria_2_6_2_form, name='criteria_2_6_2_form'),
    path('2_6_2/', criteria_2_6_2, name='criteria_2_6_2'),
    path('2_6_2/delete', criteria_2_6_2_delete, name='criteria_2_6_2_delete'),

    path('2_6_3/', criteria_2_6_3, name='criteria_2_6_3'),
    path('2_6_3/form/', criteria_2_6_3_form, name='criteria_2_6_3_form'),
    path('2_6_3/upload_excel/', upload_excel_2_6_3, name='upload_excel_2_6_3'),
    path('2_6_3/export_excel/', export_excel_2_6_3, name='export_excel_2_6_3'),

    path('2_7_1/', criteria_2_7_1, name='criteria_2_7_1'),
    path('2_7_1/form/', criteria_2_7_1_form, name='criteria_2_7_1_form'),
    path('2_7_1/upload_excel/', upload_excel_2_7_1, name='upload_excel_2_7_1'),
    path('2_7_1/export_excel/', export_excel_2_7_1, name='export_excel_2_7_1'),
]
