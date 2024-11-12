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
