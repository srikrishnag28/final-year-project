from django.shortcuts import render, redirect
from .models import *
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
from django.db.models import Sum
# Create your views here.


def criteria_4_1_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_4_1_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_4_1_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_4_1_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_4_1_1(instance=instance)

    return render(request, 'form/criteria_4_1_1.html', {'form': form})


def criteria_4_1_1(request):
    criteria_data = Criteria_4_1_1.objects.first()
    if not criteria_data:
        context = {'no_data': True}
    else:
        context = {'criteria_data': criteria_data}
    return render(request, 'table/criteria_4_1_1.html', context)


def criteria_4_1_1_delete(request):
    Criteria_4_1_1.objects.all().delete()
    return redirect('criteria_4_1_1')


def criteria_4_1_2(request):
    user = request.user
    # flag = check(user, "4_1_2")
    users = UserCriteriaLink.objects.filter(criteria="4_1_2")
    print(users)
    records_by_year = {}
    for year in [2021, 2022, 2023, 2024, 2025]:
        records = Criteria_4_1_2.objects.filter(year=year)
        total_amount = records.aggregate(total_amount=Sum('amount_in_lakhs'))['total_amount'] or 0
        records_by_year[f'{year}_records'] = {
            'records': records,
            'total': total_amount
        }
    context = {
        'users': users,
        **records_by_year,
    }
    return render(request, 'table/criteria_4_1_2.html', context=context)


def criteria_4_1_2_form(request):
    if request.method == 'POST':
        form = CriteriaForm_4_1_2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_4_1_2')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_4_1_2()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_4_1_2.html', context=context)


def upload_excel_4_1_2(request):
    pass


def export_excel_4_1_2(request):
    pass


def criteria_4_2_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_4_2_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_4_2_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_4_2_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_4_2_1(instance=instance)

    return render(request, 'form/criteria_4_2_1.html', {'form': form})


def criteria_4_2_1(request):
    criteria_data = Criteria_4_2_1.objects.first()
    if not criteria_data:
        context = {'no_data': True}
    else:
        context = {'criteria_data': criteria_data}
    return render(request, 'table/criteria_4_2_1.html', context)


def criteria_4_2_1_delete(request):
    Criteria_4_2_1.objects.all().delete()
    return redirect('criteria_4_2_1')


def criteria_4_3_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_4_3_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_4_3_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_4_3_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_4_3_1(instance=instance)

    return render(request, 'form/criteria_4_3_1.html', {'form': form})


def criteria_4_3_1(request):
    criteria_data = Criteria_4_3_1.objects.first()
    if not criteria_data:
        context = {'no_data': True}
    else:
        context = {'criteria_data': criteria_data}
    return render(request, 'table/criteria_4_3_1.html', context)


def criteria_4_3_1_delete(request):
    Criteria_4_3_1.objects.all().delete()
    return redirect('criteria_4_3_1')


def criteria_4_4_1(request):
    user = request.user
    # flag = check(user, "4_4_1")
    users = UserCriteriaLink.objects.filter(criteria="4_4_1")
    print(users)
    records_by_year = {}
    for year in [2021, 2022, 2023, 2024, 2025]:
        records = Criteria_4_4_1.objects.filter(year=year)
        total_amount = records.aggregate(total_amount=Sum('amount_in_lakhs'))['total_amount'] or 0
        records_by_year[f'{year}_records'] = {
            'records': records,
            'total': total_amount
        }
    context = {
        'users': users,
        **records_by_year,
    }
    return render(request, 'table/criteria_4_4_1.html', context=context)


def criteria_4_4_1_form(request):
    if request.method == 'POST':
        form = CriteriaForm_4_4_1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            print("ADSf")
            return redirect('criteria_4_4_1')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_4_4_1()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_4_4_1.html', context=context)


def upload_excel_4_4_1(request):
    pass


def export_excel_4_4_1(request):
    pass