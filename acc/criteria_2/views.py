from django.shortcuts import render, HttpResponse, redirect
from .models import Criteria_2_1_1, Criteria_2_7_1
from .forms import *
from datetime import datetime
from django.db import transaction
import openpyxl
from openpyxl import Workbook
from io import BytesIO
from django.contrib import messages
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill
from openpyxl.utils import get_column_letter
from user.models import UserCriteriaLink

# Create your views here.
def criteria_2_1_1(request):
    # context = {
    #     '2021_records': Criteria_2_1_1.objects.filter(year = '2021'),
    #     '2022_records': Criteria_2_1_1.objects.filter(year = '2022'),
    #     '2023_records': Criteria_2_1_1.objects.filter(year = '2023'),
    #     '2024_records': Criteria_2_1_1.objects.filter(year = '2024'),
    #     '2025_records': Criteria_2_1_1.objects.filter(year = '2025')
    # }
    # return render(request, 'table/criteria_2_7_1.html', context=context)
    pass

def criteria_2_1_1_form(request):
    # if request.method == 'POST':
    #     form = CriteriaForm_2_1_1(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Data Added Successfully')
    #         return redirect('criteria_2_1_1')
    #     else:
    #         messages.error(request, 'Enter valid Data')
    # form = CriteriaForm_2_1_1()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'form/criteria_2_7_1.html', context=context)
    pass

def upload_excel_2_1_1(request):
    pass

def export_excel_2_1_1(request):
    pass


def criteria_2_6_3(request):
    user = request.user
    users = UserCriteriaLink.objects.filter(criteria="2_6_3")
    context = {
        'users': users,
        'records': Criteria_2_6_3.objects.all(),
    }
    return render(request, 'table/criteria_2_6_3.html', context=context)

def criteria_2_6_3_form(request):
    if request.method == 'POST':
        form = CriteriaForm_2_6_3(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_2_6_3')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_2_6_3()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_2_6_3.html', context=context)

def upload_excel_2_6_3(request):
    pass

def export_excel_2_6_3(request):
    pass


def criteria_2_7_1(request):
    user = request.user
    users = UserCriteriaLink.objects.filter(criteria="2_7_1")
    context = {
        'users': users,
        'records': Criteria_2_7_1.objects.all(),
    }
    return render(request, 'table/criteria_2_7_1.html', context=context)

def criteria_2_7_1_form(request):
    if request.method == 'POST':
        form = CriteriaForm_2_7_1(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_2_7_1')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_2_7_1()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_2_7_1.html', context=context)

def upload_excel_2_7_1(request):
    pass

def export_excel_2_7_1(request):
    pass