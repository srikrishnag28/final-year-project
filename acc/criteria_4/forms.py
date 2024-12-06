from django import forms
from .models import *


class CriteriaForm_4_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_4_1_1
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


class CriteriaForm_4_1_2(forms.ModelForm):
    class Meta:
        model = Criteria_4_1_2
        fields = ['year', 'head_of_expenditure', 'item_of_expenditure', 'amount_in_lakhs']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'head_of_expenditure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Head of Expenditure'}),
            'item_of_expenditure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Item of Expenditure'}),
            'amount_in_lakhs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount in Lakhs'}),
        }


class CriteriaForm_4_2_1(forms.ModelForm):
    class Meta:
        model = Criteria_4_2_1
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


class CriteriaForm_4_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_4_3_1
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


class CriteriaForm_4_4_1(forms.ModelForm):
    class Meta:
        model = Criteria_4_4_1
        fields = ['year', 'head_of_expenditure', 'item_of_expenditure', 'amount_in_lakhs']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'head_of_expenditure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Head of Expenditure'}),
            'item_of_expenditure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Item of Expenditure'}),
            'amount_in_lakhs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount in Lakhs'}),
        }
