from django import forms
from .models import *


class CriteriaForm_1_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_1_1_1
        fields = ['description', 'additional_information_file', 'additional_information_link']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': '4',
            'id': 'description',
            'required': True,
            'placeholder': (
                'Describe in a maximum of 500 words.'
            )
        })
    )
    additional_information_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control mb-3',
            'id': 'fileUpload',
            'accept': '.pdf, .docx, .xlsx'
        })
    )
    additional_information_link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )


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


class CriteriaForm_1_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_1_3_1
        fields = ['description', 'additional_information_file', 'additional_information_link']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': '4',
            'id': 'description',
            'required': True,
            'placeholder': (
                'Describe in a maximum of 500 words.'
            )
        })
    )
    additional_information_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control mb-3',
            'id': 'fileUpload',
            'accept': '.pdf, .docx, .xlsx'
        })
    )
    additional_information_link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )


class CriteriaForm_1_3_2(forms.ModelForm):
    class Meta:
        model = Criteria_1_3_2
        fields = [
            'programme_name', 'programme_code', 'student_list', 'document_link'
        ]
        widgets = {
            'programme_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Programme Name'}),
            'programme_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Programme Code'}),
            'student_list': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter List of Students'}),
            'document_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Document Link'}),
        }
