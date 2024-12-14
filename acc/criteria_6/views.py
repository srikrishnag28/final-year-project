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

# Create your views here.


@login_required
def criteria_6_1_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_6_1_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_6_1_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_6_1_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_6_1_1(instance=instance)

    return render(request, 'form/criteria_6_1_1.html', {'form': form})


@login_required
def criteria_6_1_1(request):
    criteria_data = Criteria_6_1_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_1_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_1_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_6_1_1.html', context)


@login_required
def criteria_6_1_1_delete(request):
    Criteria_6_1_1.objects.all().delete()
    return redirect('criteria_6_1_1')


@login_required
def criteria_6_2_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_6_2_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_6_2_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_6_2_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_6_2_1(instance=instance)

    return render(request, 'form/criteria_6_2_1.html', {'form': form})


@login_required
def criteria_6_2_1(request):
    criteria_data = Criteria_6_2_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_2_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_2_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_6_2_1.html', context)


@login_required
def criteria_6_2_1_delete(request):
    Criteria_6_2_1.objects.all().delete()
    return redirect('criteria_6_2_1')


@login_required
def criteria_6_2_2(request):
    criteria_data = Criteria_6_2_2.objects.first()
    flag = UserCriteriaLink.objects.filter(user=request.user, criteria='6_2_2').exists()
    if request.method == 'POST':
        form = CriteriaForm_6_2_2(request.POST)
        if form.is_valid():
            if criteria_data:
                form.instance.pk = criteria_data.pk
            form.save()
            messages.success(request, 'Data Added/Updated Successfully')
            return redirect('criteria_6_2_2')
        else:
            messages.error(request, 'Please enter valid data.')
    form = CriteriaForm_6_2_2(instance=criteria_data) if criteria_data else CriteriaForm_6_2_2()
    context = {
        'form': form,
        'criteria_data': criteria_data,
        'flag': flag,
    }
    return render(request, 'table/criteria_6_2_2.html', context)


@login_required
def criteria_6_3_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_6_3_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_6_3_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_6_3_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_6_3_1(instance=instance)

    return render(request, 'form/criteria_6_3_1.html', {'form': form})


@login_required
def criteria_6_3_1(request):
    criteria_data = Criteria_6_3_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_3_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_3_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_6_3_1.html', context)


@login_required
def criteria_6_3_1_delete(request):
    Criteria_6_3_1.objects.all().delete()
    return redirect('criteria_6_3_1')


@login_required
def criteria_6_3_2(request):
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_3_2').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_3_2")
    context = {
        'has_access': has_access,
        'users': users,
        'records': Criteria_6_3_2.objects.all(),
    }
    return render(request, 'table/criteria_6_3_2.html', context=context)


@login_required
def criteria_6_3_2_form(request):
    if request.method == 'POST':
        form = CriteriaForm_6_3_2(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_6_3_2')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_6_3_2()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_6_3_2.html', context=context)


@login_required
def upload_excel_6_3_2(request):
    pass


@login_required
def export_excel_6_3_2(request):
    pass


@login_required
def criteria_6_3_3(request):
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_3_3').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_3_3")
    context = {
        'has_access': has_access,
        'users': users,
        'records': Criteria_6_3_3.objects.all(),
    }
    return render(request, 'table/criteria_6_3_3.html', context=context)


@login_required
def criteria_6_3_3_form(request):
    if request.method == 'POST':
        form = CriteriaForm_6_3_3(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_6_3_3')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_6_3_3()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_6_3_3.html', context=context)


@login_required
def upload_excel_6_3_3(request):
    pass


@login_required
def export_excel_6_3_3(request):
    pass


@login_required
def criteria_6_4_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_6_4_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_6_4_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_6_4_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_6_4_1(instance=instance)

    return render(request, 'form/criteria_6_4_1.html', {'form': form})


@login_required
def criteria_6_4_1(request):
    criteria_data = Criteria_6_4_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_4_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_4_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_6_4_1.html', context)


@login_required
def criteria_6_4_1_delete(request):
    Criteria_6_4_1.objects.all().delete()
    return redirect('criteria_6_4_1')


@login_required
def criteria_6_5_1_form(request):
    # Get the existing instance (if any)
    instance = Criteria_6_5_1.objects.first()

    if request.method == 'POST':
        form = CriteriaForm_6_5_1(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('criteria_6_5_1')
        else:
            print(form.errors)
    else:
        form = CriteriaForm_6_5_1(instance=instance)

    return render(request, 'form/criteria_6_5_1.html', {'form': form})


@login_required
def criteria_6_5_1(request):
    criteria_data = Criteria_6_5_1.objects.first()
    has_access = UserCriteriaLink.objects.filter(user=request.user, criteria='6_5_1').exists()
    users = UserCriteriaLink.objects.filter(criteria="6_5_1")
    context = {
        'criteria_data': criteria_data,
        'has_access': has_access,
        'users': users,
    }
    if not criteria_data:
        context['no_data'] = True
    return render(request, 'table/criteria_6_5_1.html', context)


@login_required
def criteria_6_5_1_delete(request):
    Criteria_6_5_1.objects.all().delete()
    return redirect('criteria_6_5_1')


@login_required
def criteria_6_5_2(request):
    criteria_data = Criteria_6_5_2.objects.first()
    flag = UserCriteriaLink.objects.filter(user=request.user, criteria='6_5_2').exists()
    if request.method == 'POST':
        form = CriteriaForm_6_5_2(request.POST)
        if form.is_valid():
            if criteria_data:
                form.instance.pk = criteria_data.pk
            form.save()
            messages.success(request, 'Data Added/Updated Successfully')
            return redirect('criteria_6_5_2')
        else:
            messages.error(request, 'Please enter valid data.')
    form = CriteriaForm_6_5_2(instance=criteria_data) if criteria_data else CriteriaForm_6_5_2()
    context = {
        'form': form,
        'criteria_data': criteria_data,
        'flag': flag,
    }
    return render(request, 'table/criteria_6_5_2.html', context)