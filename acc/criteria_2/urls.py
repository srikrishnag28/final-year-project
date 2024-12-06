from django.urls import path
from .views import *

urlpatterns = [
    path('2_1_1/', criteria_2_1_1, name='criteria_2_1_1'),
    path('2_1_1/form/', criteria_2_1_1_form, name='criteria_2_1_1_form'),
    path('2_1_1/upload_excel/', upload_excel_2_1_1, name='upload_excel_2_1_1'),
    path('2_1_1/export_excel/', export_excel_2_1_1, name='export_excel_2_1_1'),

    path('2_6_3/', criteria_2_6_3, name='criteria_2_6_3'),
    path('2_6_3/form/', criteria_2_6_3_form, name='criteria_2_6_3_form'),
    path('2_6_3/upload_excel/', upload_excel_2_6_3, name='upload_excel_2_6_3'),
    path('2_6_3/export_excel/', export_excel_2_6_3, name='export_excel_2_6_3'),

    path('2_7_1/', criteria_2_7_1, name='criteria_2_7_1'),
    path('2_7_1/form/', criteria_2_7_1_form, name='criteria_2_7_1_form'),
    path('2_7_1/upload_excel/', upload_excel_2_7_1, name='upload_excel_2_7_1'),
    path('2_7_1/export_excel/', export_excel_2_7_1, name='export_excel_2_7_1'),
]
