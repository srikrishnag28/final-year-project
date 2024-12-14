from django import forms
from .models import *


class CriteriaForm_7_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_7_1_1
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

    class CriteriaForm_7_1_1(forms.ModelForm):
        class Meta:
            model = Criteria_7_1_1
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
      

class CriteriaForm_7_1_2(forms.ModelForm):
    class Meta:
        model = Criteria_7_1_2
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_7_1_2.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )


class CriteriaForm_7_1_3(forms.ModelForm):
    class Meta:
        model = Criteria_7_1_3
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_7_1_3.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )

        
class CriteriaForm_7_1_4(forms.ModelForm):
    class Meta:
        model = Criteria_7_1_4
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


class CriteriaForm_7_2_1(forms.ModelForm):
    class Meta:
        model = Criteria_7_2_1
        fields = ['description', 'weblink_to_institutional_website', 'weblink_to_other_relevant_info']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': '4',
            'id': 'description',
            'required': True,
            'placeholder': (
                'Describe in a maximum of 1000 words.'
            )
        })
    )
    weblink_to_institutional_website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )
    weblink_to_other_relevant_info = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )


class CriteriaForm_7_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_7_3_1
        fields = ['description', 'weblink_to_institutional_website', 'weblink_to_other_relevant_info']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'rows': '4',
            'id': 'description',
            'required': True,
            'placeholder': (
                'Describe in a maximum of 1000 words.'
            )
        })
    )
    weblink_to_institutional_website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )
    weblink_to_other_relevant_info = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )