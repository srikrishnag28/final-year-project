from django.shortcuts import render, HttpResponse, redirect
from .models import Criteria_3_1_1, Criteria_3_2_2
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


def check(user, criteria):
    temp = UserCriteriaLink.objects.filter(user=user, criteria=criteria)
    print(temp)
    if not temp.exists():
        return False
    return True


def criteria_3_1_1(request):
    user = request.user
    flag = check(user, "3_1_1")
    users = UserCriteriaLink.objects.filter(criteria="3_1_1")
    print(users)
    print(flag)
    context = {
        'flag': flag,
        'users': users,
        '2021_records': Criteria_3_1_1.objects.filter(year = '2021'),
        '2022_records': Criteria_3_1_1.objects.filter(year = '2022'),
        '2023_records': Criteria_3_1_1.objects.filter(year = '2023'),
        '2024_records': Criteria_3_1_1.objects.filter(year = '2024'),
        '2025_records': Criteria_3_1_1.objects.filter(year = '2025')
    }
    return render(request, 'table/criteria_3_1_1.html', context=context)


def criteria_3_1_1_form(request):
    if request.method == 'POST':
        form = CriteriaForm_3_1_1(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_3_1_1')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_3_1_1()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_3_1_1.html', context=context)

def upload_excel_3_1_1(request):
    pass

def export_excel_3_1_1(request):
    pass

def criteria_3_2_2(request):
    user = request.user
    flag = check(user, "3_2_2")
    users = UserCriteriaLink.objects.filter(criteria="3_2_2")
    context = {
        'flag': flag,
        'users': users,
        '2021_records': Criteria_3_2_2.objects.filter(year = '2021'),
        '2022_records': Criteria_3_2_2.objects.filter(year = '2022'),
        '2023_records': Criteria_3_2_2.objects.filter(year = '2023'),
        '2024_records': Criteria_3_2_2.objects.filter(year = '2024'),
        '2025_records': Criteria_3_2_2.objects.filter(year = '2025')
    }
    return render(request, 'table/criteria_3_2_2.html', context=context)

def criteria_3_2_2_form(request):
    if request.method == 'POST':
        form = CriteriaForm_3_2_2(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_3_2_2')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_3_2_2()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_3_2_2.html', context=context)

def upload_excel_3_2_2(request):
    pass

def export_excel_3_2_2(request):
    pass


def criteria_3_3_1(request):
    user = request.user
    flag = check(user, "3_3_1")
    users = UserCriteriaLink.objects.filter(criteria="3_3_1")
    context = {
        'flag': flag,
        'users': users,
        '2021_records': Criteria_3_3_1.objects.filter(year = '2021'),
        '2022_records': Criteria_3_3_1.objects.filter(year = '2022'),
        '2023_records': Criteria_3_3_1.objects.filter(year = '2023'),
        '2024_records': Criteria_3_3_1.objects.filter(year = '2024'),
        '2025_records': Criteria_3_3_1.objects.filter(year = '2025')
    }
    return render(request, 'table/criteria_3_3_1.html', context=context)

def criteria_3_3_1_form(request):
    if request.method == 'POST':
        form = CriteriaForm_3_3_1(request.POST)
        print(form.data)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_3_3_1')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_3_3_1()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_3_3_1.html', context=context)

def upload_excel_3_3_1(request):
    pass

def export_excel_3_3_1(request):
    pass


def criteria_3_5_1(request):
    user = request.user
    flag = check(user, "3_5_1")
    users = UserCriteriaLink.objects.filter(criteria="3_5_1")
    context = {
        'flag': flag,
        'users': users,
        '2021_records': Criteria_3_5_1.objects.filter(year = '2021'),
        '2022_records': Criteria_3_5_1.objects.filter(year = '2022'),
        '2023_records': Criteria_3_5_1.objects.filter(year = '2023'),
        '2024_records': Criteria_3_5_1.objects.filter(year = '2024'),
        '2025_records': Criteria_3_5_1.objects.filter(year = '2025')
    }
    return render(request, 'table/criteria_3_5_1.html', context=context)

def criteria_3_5_1_form(request):
    if request.method == 'POST':
        form = CriteriaForm_3_5_1(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_3_5_1')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_3_5_1()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_3_5_1.html', context=context)

def upload_excel_3_5_1(request):
    pass

def export_excel_3_5_1(request):
    pass
