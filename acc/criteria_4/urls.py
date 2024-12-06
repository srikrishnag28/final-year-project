from django.urls import path
from .views import *

urlpatterns = [
    path('4_1_1/form/', criteria_4_1_1_form, name='criteria_4_1_1_form'),
    path('4_1_1/', criteria_4_1_1, name='criteria_4_1_1'),
    path('4_1_1/delete', criteria_4_1_1_delete, name='criteria_4_1_1_delete'),

    path('4_2_1/form/', criteria_4_2_1_form, name='criteria_4_2_1_form'),
    path('4_2_1/', criteria_4_2_1, name='criteria_4_2_1'),
    path('4_2_1/delete', criteria_4_2_1_delete, name='criteria_4_2_1_delete'),
    
    path('4_1_2/', criteria_4_1_2, name='criteria_4_1_2'),
    path('4_1_2/form/', criteria_4_1_2_form, name='criteria_4_1_2_form'),
    path('4_1_2/upload_excel/', upload_excel_4_1_2, name='upload_excel_4_1_2'),
    path('4_1_2/export_excel/', export_excel_4_1_2, name='export_excel_4_1_2'),

    path('4_3_1/form/', criteria_4_3_1_form, name='criteria_4_3_1_form'),
    path('4_3_1/', criteria_4_3_1, name='criteria_4_3_1'),
    path('4_3_1/delete', criteria_4_3_1_delete, name='criteria_4_3_1_delete'),

    path('4_4_1/', criteria_4_4_1, name='criteria_4_4_1'),
    path('4_4_1/form/', criteria_4_4_1_form, name='criteria_4_4_1_form'),
    path('4_4_1/upload_excel/', upload_excel_4_4_1, name='upload_excel_4_4_1'),
    path('4_4_1/export_excel/', export_excel_4_4_1, name='export_excel_4_4_1'),
]