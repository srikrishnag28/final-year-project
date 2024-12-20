from django import forms
from .models import *

class CriteriaForm_3_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_1_1
        fields = ['year', 'project_name', 'principal_investigator', 'department', 'year_of_award', 'amount_sanctioned', 'duration', 'funding_agency', 
    'grant_type' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'grant_type': forms.Select(attrs={'class': 'form-select'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Name'}),
            'principal_investigator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Principal Investigator'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Duration'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'year_of_award': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Award'}),
            'amount_sanctioned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount Sanctioned'}),
            'funding_agency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Funding Agency'}),
        }


class CriteriaForm_3_2_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_2_1
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


class CriteriaForm_3_2_2(forms.ModelForm):
    class Meta:
        model = Criteria_3_2_2
        fields = [ 'year', 'event_name', 'num_participants', 'date_from', 'date_to', 'activity_report_link' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Event Name'}),
            'num_participants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Participants'}),
            'date_from': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'date_to': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'activity_report_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Link '}),
        }


class CriteriaForm_3_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_3_1
        fields = [
            'year', 'title_of_paper', 'authors', 'department', 
            'journal_name', 'year_of_publication', 'issn_number', 
            'journal_website_link', 'article_link', 'is_ugc_care_listed'
        ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'title_of_paper': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of Paper'}),
            'authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Authors'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'journal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Journal Name'}),
            'year_of_publication': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Publication'}),
            'issn_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISSN Number'}),
            'journal_website_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Journal Website Link'}),
            'article_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Article Link'}),
            'is_ugc_care_listed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CriteriaForm_3_3_2(forms.ModelForm):
    class Meta:
        model = Criteria_3_3_2
        fields = [
            'name_of_teacher',
            'title_of_book_or_chapters_published',
            'title_of_paper',
            'title_of_proceedings_of_conference',
            'name_of_conference',
            'national_or_international',
            'calendar_year_of_publication',
            'isbn_number_of_proceeding',
            'affiliating_institute_at_time_of_publication',
            'name_of_publisher'
        ]
        widgets = {
            'name_of_teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Teacher'}),
            'title_of_book_or_chapters_published': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of Book or Chapters Published'}),
            'title_of_paper': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of Paper'}),
            'title_of_proceedings_of_conference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of Proceedings'}),
            'name_of_conference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Conference'}),
            'national_or_international': forms.Select(attrs={'class': 'form-select'}),
            'calendar_year_of_publication': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Publication'}),
            'isbn_number_of_proceeding': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN Number'}),
            'affiliating_institute_at_time_of_publication': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Affiliating Institute'}),
            'name_of_publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Publisher'}),
        }


class CriteriaForm_3_4_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_4_1
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


class CriteriaForm_3_4_2(forms.ModelForm):
    class Meta:
        model = Criteria_3_4_2
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


class CriteriaForm_3_4_3(forms.ModelForm):
    class Meta:
        model = Criteria_3_4_3
        fields = ['name_of_activity', 'organising_unit_or_agency_or_collaborating_agency', 'name_of_scheme', 'year_of_activity']
        widgets = {
            'name_of_activity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Activity'}),
            'organising_unit_or_agency_or_collaborating_agency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Organising Unit/Agency'}),
            'name_of_scheme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Scheme'}),
            'year_of_activity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Activity'}),
        }


class CriteriaForm_3_5_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_5_1
        fields = ['year', 'mou_name', 'institution_name', 'signing_year', 'pourpose', 'duration', 'activities', 
    'document_link' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'mou_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter MOU Name'}),
            'institution_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Name'}),
            'signing_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Signing Year'}),
            'pourpose': forms.Select(attrs={'class': 'form-select'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Duration'}),
            'activities': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Activities'}),
            'document_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Document Link'}),
        }
