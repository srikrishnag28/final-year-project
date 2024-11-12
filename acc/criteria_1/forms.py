from django import forms
from .models import Criteria_1_2_2

class CriteriaForm_1_2_2(forms.ModelForm):
    class Meta:
        model = Criteria_1_2_2
        fields = ['year', 'course_name', 'course_code', 'year_of_study', 'period_from', 'period_to', 'duration', 'students_enrolled', 'students_completed']
        widgets = {
            'period_from': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'DD/MM/YYYY', 'autocomplete': 'off'}),
            'period_to': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'DD/MM/YYYY', 'autocomplete': 'off'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'course_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Code'}),
            'year_of_study': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Study'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Duration'}),
            'students_enrolled': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Enrolled'}),
            'students_completed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Completed'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value of period_from and period_to to None (empty)
        self.fields['period_from'].initial = None
        self.fields['period_to'].initial = None


