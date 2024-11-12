from django.urls import path
from .views import *

urlpatterns = [
    path('temp/', render_temp),
    path('1_2_2/', criteria_1_2_2, name='criteria_1_2_2'),
    path('1_2_2/form/', criteria_1_2_2_form, name='criteria_1_2_2_form'),
    path('1_2_2/upload_excel/', upload_excel_1_2_2, name='upload_excel_1_2_2'),
    path('1_2_2/export_excel/', export_excel_1_2_2, name='export_excel_1_2_2'),
]