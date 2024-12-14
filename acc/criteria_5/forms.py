from django import forms
from .models import *


class CriteriaForm_5_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_5_1_1
        fields = [
            'year', 'scheme_name', 'government_or_non_government',
            'individual_or_organization_name', 'number_of_students_benefited',
            'amount_in_inr'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'scheme_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of the Scheme'}),
            'government_or_non_government': forms.Select(attrs={'class': 'form-select'}),
            'individual_or_organization_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of the Individual/Organization'}),
            'number_of_students_benefited': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Benefited'}),
            'amount_in_inr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount (in INR)'}),
        }


class CriteriaForm_5_1_2(forms.ModelForm):
    class Meta:
        model = Criteria_5_1_2
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_5_1_2.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )


class CriteriaForm_5_1_3(forms.ModelForm):
    class Meta:
        model = Criteria_5_1_3
        fields = [
            'year',
            'guidance_activity_name', 'guidance_students_participated', 'guidance_students_qualified',
            'counselling_activity_name', 'counselling_students_participated', 'counselling_students_placed'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'guidance_activity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Guidance Activity Name'}),
            'guidance_students_participated': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Participated'}),
            'guidance_students_qualified': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Qualified'}),
            'counselling_activity_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Counselling Activity Name'}),
            'counselling_students_participated': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Participated'}),
            'counselling_students_placed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Students Placed'}),
        }


class CriteriaForm_5_1_4(forms.ModelForm):
    class Meta:
        model = Criteria_5_1_4
        fields = ['selected_option']

    selected_option = forms.ChoiceField(
        choices=Criteria_5_1_4.OPTION_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
            'id': 'selectedOption',
            'required': True,
        }),
        label="Select Option",
    )


class CriteriaForm_5_2_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_5_2_1_1
        fields = [
            'year', 'student_name', 'program_graduated_from',
            'year_of_graduation', 'employer_name_with_contact', 'pay_package_per_annum'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'program_graduated_from': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Graduated From'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Graduation'}),
            'employer_name_with_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employer Details'}),
            'pay_package_per_annum': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pay Package (INR per annum)'}),
        }


class CriteriaForm_5_2_1_2(forms.ModelForm):
    class Meta:
        model = Criteria_5_2_1_2
        fields = [
            'year', 'student_name', 'program_graduated_from',
            'year_of_graduation', 'institution_joined', 'program_admitted_to'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'program_graduated_from': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Graduated From'}),
            'year_of_graduation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Graduation'}),
            'institution_joined': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Joined'}),
            'program_admitted_to': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Program Admitted To'}),
        }


class CriteriaForm_5_2_2(forms.ModelForm):
    class Meta:
        model = Criteria_5_2_2
        fields = [
            'year', 'registration_or_roll_number', 'student_name', 'qualifying_exam_name'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'registration_or_roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registration or Roll Number'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'qualifying_exam_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Qualifying Exam Name'}),
        }


class CriteriaForm_5_3_1(forms.ModelForm):
    class Meta:
        model = Criteria_5_3_1
        fields = ['year', 'name_of_award_medal', 'team_or_individual', 'level_of_competition', 'nature_of_competition', 'name_of_students']
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the academic year (e.g., 2023)'}),
            'name_of_award_medal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the award or medal'}),
            'team_or_individual': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select whether it was a team or individual'}),
            'level_of_competition': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select the level of competition'}),
            'nature_of_competition': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select the nature of competition (e.g., Sports)'}),
            'name_of_students': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the names of the students, separated by commas', 'rows': 3}),
        }

class CriteriaForm_5_3_2(forms.ModelForm):
    class Meta:
        model = Criteria_5_3_2
        fields = ['year', 'date_of_event', 'name_of_event', 'name_of_organising_institution', 'name_of_student_participated']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select the academic year'}),
            'date_of_event': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select the date of the event/activity', 'type': 'date'}),
            'name_of_event': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the event or activity'}),
            'name_of_organising_institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the organising institution'}),
            'name_of_student_participated': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the names of participating students, separated by commas', 'rows': 3}),
        }


class CriteriaForm_5_4_1(forms.ModelForm):
    class Meta:
        model = Criteria_5_4_1
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
