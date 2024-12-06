from django import forms
from .models import *

class CriteriaForm_2_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_2_1_1
        fields = [
            'year', 'programme_name', 'programme_code', 'number_of_seats_sanctioned', 'number_of_students_admitted',
            'seats_earmarked_sc', 'seats_earmarked_st', 'seats_earmarked_obc', 'seats_earmarked_gen', 'seats_earmarked_others',
            'students_admitted_sc', 'students_admitted_st', 'students_admitted_obc', 'students_admitted_gen', 'students_admitted_others'
        ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'programme_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Programme Name'}),
            'programme_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Programme Code'}),
            'number_of_seats_sanctioned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Seats Sanctioned'}),
            'number_of_students_admitted': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Admitted'}),
            'seats_earmarked_sc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seats Earmarked for SC'}),
            'seats_earmarked_st': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seats Earmarked for ST'}),
            'seats_earmarked_obc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seats Earmarked for OBC'}),
            'seats_earmarked_gen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seats Earmarked for General'}),
            'seats_earmarked_others': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seats Earmarked for Others'}),
            'students_admitted_sc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Students Admitted from SC'}),
            'students_admitted_st': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Students Admitted from ST'}),
            'students_admitted_obc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Students Admitted from OBC'}),
            'students_admitted_gen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Students Admitted from General'}),
            'students_admitted_others': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Students Admitted from Others'}),
        }


class CriteriaForm_2_6_3(forms.ModelForm):
    class Meta:
        model = Criteria_2_6_3
        fields = ['year', 'program_code', 'program_name', 'number_of_students_appeared', 'number_of_students_passed']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'program_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Code'}),
            'program_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Name'}),
            'number_of_students_appeared': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Appeared'}),
            'number_of_students_passed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Passed'}),
        }


class CriteriaForm_2_7_1(forms.ModelForm):
    class Meta:
        model = Criteria_2_7_1
        fields = [
            'name', 'gender', 'category', 'state_of_domicile',
            'nationality', 'email', 'program_name',
            'enrolment_id', 'year_of_joining'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category'}),
            'state_of_domicile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State of Domicile'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nationality'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'program_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Name'}),
            'enrolment_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Enrolment ID'}),
            'year_of_joining': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Joining'}),
        }


