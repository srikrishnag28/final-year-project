from django import forms
from .models import *


class CriteriaForm_6_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_6_1_1
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


class CriteriaForm_6_2_1(forms.ModelForm):
    class Meta:
        model = Criteria_6_2_1
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


class CriteriaForm_6_2_2(forms.ModelForm):
    class Meta:
        model = Criteria_6_2_2
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_6_2_2.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )


class CriteriaForm_6_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_6_3_1
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


class CriteriaForm_6_3_2(forms.ModelForm):
    class Meta:
        model = Criteria_6_3_2
        fields = [
            'year', 'name_of_teacher', 'name_of_conference_or_workshop',
            'name_of_professional_body', 'amount_of_support_received_in_inr'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'name_of_teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Teacher'}),
            'name_of_conference_or_workshop': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Conference/Workshop'}),
            'name_of_professional_body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Professional Body'}),
            'amount_of_support_received_in_inr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount (in INR)'}),
        }


class CriteriaForm_6_3_3(forms.ModelForm):
    class Meta:
        model = Criteria_6_3_3
        fields = [
            'year', 'name_of_participant', 'designation',
            'title_of_program', 'date_from', 'date_to'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'name_of_participant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Participant'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation'}),
            'title_of_program': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of the Program'}),
            'date_from': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Start Date (DD-MM-YYYY)', 'type': 'date'}),
            'date_to': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter End Date (DD-MM-YYYY)', 'type': 'date'}),
        }


class CriteriaForm_6_4_1(forms.ModelForm):
    class Meta:
        model = Criteria_6_4_1
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
    

class CriteriaForm_6_5_1(forms.ModelForm):
    class Meta:
        model = Criteria_6_5_1
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
    
    
class CriteriaForm_6_5_2(forms.ModelForm):
    class Meta:
        model = Criteria_6_5_2
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_6_5_2.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )