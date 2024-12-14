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
from django.contrib.auth.decorators import login_required


@login_required
def criteria_7_1_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_7_1_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_7_1_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_7_1_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_7_1_1(instance=instance)

    return render(request, 'form/criteria_7_1_1.html', {'form': form})


@login_required
def criteria_7_1_1(request):
    criteria_data = Criteria_7_1_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='7_1_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="7_1_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_7_1_1.html', context)


@login_required
def criteria_7_1_1_delete(request):
    Criteria_7_1_1.objects.all().delete()
    return redirect('criteria_7_1_1')


@login_required
def criteria_7_1_2(request):
    criteria_data = Criteria_7_1_2.objects.first()
    flag = UserCriteriaLink.objects.filter(user=request.user, criteria='7_1_2').exists()
    if request.method == 'POST':
        form = CriteriaForm_7_1_2(request.POST)
        if form.is_valid():
            if criteria_data:
                form.instance.pk = criteria_data.pk
            form.save()
            messages.success(request, 'Data Added/Updated Successfully')
            return redirect('criteria_7_1_2')
        else:
            messages.error(request, 'Please enter valid data.')
    form = CriteriaForm_7_1_2(instance=criteria_data) if criteria_data else CriteriaForm_7_1_2()
    context = {
        'form': form,
        'criteria_data': criteria_data,
        'flag': flag,
    }
    return render(request, 'table/criteria_7_1_2.html', context)


@login_required
def criteria_7_1_3(request):
    criteria_data = Criteria_7_1_3.objects.first()
    flag = UserCriteriaLink.objects.filter(user=request.user, criteria='7_1_3').exists()
    if request.method == 'POST':
        form = CriteriaForm_7_1_3(request.POST)
        if form.is_valid():
            if criteria_data:
                form.instance.pk = criteria_data.pk
            form.save()
            messages.success(request, 'Data Added/Updated Successfully')
            return redirect('criteria_7_1_3')
        else:
            messages.error(request, 'Please enter valid data.')
    form = CriteriaForm_7_1_3(instance=criteria_data) if criteria_data else CriteriaForm_7_1_3()
    context = {
        'form': form,
        'criteria_data': criteria_data,
        'flag': flag,
    }
    return render(request, 'table/criteria_7_1_3.html', context)


@login_required
def criteria_7_1_4_form(request):
    # Get the existing instance (if any)
    instance = Criteria_7_1_4.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_7_1_4(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_7_1_4')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_7_1_4(instance=instance)

    return render(request, 'form/criteria_7_1_4.html', {'form': form})


@login_required
def criteria_7_1_4(request):
    criteria_data = Criteria_7_1_4.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='7_1_4').exists()
    users = UserCriteriaLink.objects.filter(criteria="7_1_4")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_7_1_4.html', context)


@login_required
def criteria_7_1_4_delete(request):
    Criteria_7_1_4.objects.all().delete()
    return redirect('criteria_7_1_4')


@login_required
def criteria_7_2_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_7_2_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_7_2_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_7_2_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_7_2_1(instance=instance)

    return render(request, 'form/criteria_7_2_1.html', {'form': form})


@login_required
def criteria_7_2_1(request):
    criteria_data = Criteria_7_2_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='7_2_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="7_2_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_7_2_1.html', context)


@login_required
def criteria_7_2_1_delete(request):
    Criteria_7_2_1.objects.all().delete()
    return redirect('criteria_7_2_1')


@login_required
def criteria_7_3_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_7_3_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_7_3_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_7_3_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_7_3_1(instance=instance)

    return render(request, 'form/criteria_7_3_1.html', {'form': form})


@login_required
def criteria_7_3_1(request):
    criteria_data = Criteria_7_3_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='7_3_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="7_3_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_7_3_1.html', context)


@login_required
def criteria_7_3_1_delete(request):
    Criteria_7_3_1.objects.all().delete()
    return redirect('criteria_7_3_1')