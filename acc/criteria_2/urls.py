from django.urls import path
from .views import *

urlpatterns = [
    path('2_1_1/', criteria_2_1_1, name='criteria_2_1_1'),
    path('2_1_1/form/', criteria_2_1_1_form, name='criteria_2_1_1_form'),
    path('2_1_1/upload_excel/', upload_excel_2_1_1, name='upload_excel_2_1_1'),
    path('2_1_1/export_excel/', export_excel_2_1_1, name='export_excel_2_1_1'),
]
