from django import forms
from .models import Criteria_4_1_1


class Criteria_4_1_1Form(forms.ModelForm):
    class Meta:
        model = Criteria_4_1_1
        fields = ['description', 'additional_information_file', 'additional_information_link']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',  # Added bottom margin for spacing
            'rows': '4',
            'id': 'description',
            'required': True,
            'placeholder': 'Describe the adequacy of facilities such as classrooms, laboratories, ICT-enabled facilities, cultural and sports activities, etc. in a maximum of 500 words.'
        })
    )
    additional_information_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control mb-3',  # Added bottom margin for spacing
            'id': 'fileUpload',
            'accept': '.pdf, .docx, .xlsx'
        })
    )
    additional_information_link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',  # Added bottom margin for spacing
            'id': 'relatedLink',
            'placeholder': 'https://example.com'
        })
    )
