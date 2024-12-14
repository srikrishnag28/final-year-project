from django.db import models
from django.core.exceptions import ValidationError

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 500:
        raise ValidationError(f'Description cannot exceed 500 words. Current word count: {word_count}')

class Criteria_2_1_1(models.Model):
    YEAR_CHOICES = [
        (2021, 'JUN-2021 - MAY-2022'),
        (2022, 'JUN-2022 - MAY-2023'),
        (2023, 'JUN-2023 - MAY-2024'),
        (2024, 'JUN-2024 - MAY-2025'),
        (2025, 'JUN-2025 - MAY-2026'),
    ]
    
    year = models.IntegerField(choices=YEAR_CHOICES)
    programme_name = models.CharField(max_length=255)
    programme_code = models.CharField(max_length=50)
    number_of_seats_sanctioned = models.PositiveIntegerField()
    number_of_students_admitted = models.PositiveIntegerField()
    
    # Seats earmarked for reserved categories
    seats_earmarked_sc = models.PositiveIntegerField()
    seats_earmarked_st = models.PositiveIntegerField()
    seats_earmarked_obc = models.PositiveIntegerField()
    seats_earmarked_gen = models.PositiveIntegerField()
    seats_earmarked_others = models.PositiveIntegerField()
    
    # Students admitted from reserved categories
    students_admitted_sc = models.PositiveIntegerField()
    students_admitted_st = models.PositiveIntegerField()
    students_admitted_obc = models.PositiveIntegerField()
    students_admitted_gen = models.PositiveIntegerField()
    students_admitted_others = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.programme_name} ({self.get_year_display()})"
    

class Criteria_2_1_2(models.Model):
    YEAR_CHOICES = [
        (2021, 'JUN-2021 - MAY-2022'),
        (2022, 'JUN-2022 - MAY-2023'),
        (2023, 'JUN-2023 - MAY-2024'),
        (2024, 'JUN-2024 - MAY-2025'),
        (2025, 'JUN-2025 - MAY-2026'),
    ]
    
    year = models.IntegerField(choices=YEAR_CHOICES)
    programme_name = models.CharField(max_length=255)
    programme_code = models.CharField(max_length=50)
    number_of_seats_sanctioned = models.PositiveIntegerField()
    number_of_students_admitted = models.PositiveIntegerField()
    
    # Seats earmarked for reserved categories
    seats_earmarked_sc = models.PositiveIntegerField()
    seats_earmarked_st = models.PositiveIntegerField()
    seats_earmarked_obc = models.PositiveIntegerField()
    seats_earmarked_gen = models.PositiveIntegerField()
    seats_earmarked_others = models.PositiveIntegerField()
    
    # Students admitted from reserved categories
    students_admitted_sc = models.PositiveIntegerField()
    students_admitted_st = models.PositiveIntegerField()
    students_admitted_obc = models.PositiveIntegerField()
    students_admitted_gen = models.PositiveIntegerField()
    students_admitted_others = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.programme_name} ({self.get_year_display()})"
    

class Criteria_2_3_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_2/2_3_1/',
        blank=True,
        null=True,
        help_text="Upload any additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide the link for additional information."
    )

    def save(self, *args, **kwargs):
        if Criteria_2_3_1.objects.exists():
            existing = Criteria_2_3_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link']
                )
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]


class Criteria_2_4_2_1(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50)
    vidwan_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    designation = models.CharField(max_length=255)
    date_of_joining_institution = models.DateField()
    nature_of_appointment = models.CharField(
        max_length=50,
        choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')]
    )
    department_name = models.CharField(max_length=255)
    highest_qualification = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id_number}) - {self.designation}"


class Criteria_2_4_2_2(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50, blank=True, null=True)
    vidwan_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    designation = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField(blank=True, null=True)
    nature_of_appointment = models.CharField(
        max_length=50,
        choices=[
            ('Against Sanctioned Post', 'Against Sanctioned Post'),
            ('Temporary', 'Temporary'),
            ('Permanent', 'Permanent')
        ]
    )
    department_name = models.CharField(max_length=255)
    highest_qualification = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id_number}) - {self.designation}"
    

class Criteria_2_5_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_2/2_5_1/',
        blank=True,
        null=True,
        help_text="Upload any additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide the link for additional information."
    )

    def save(self, *args, **kwargs):
        if Criteria_2_5_1.objects.exists():
            existing = Criteria_2_5_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link']
                )
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]
    
    
class Criteria_2_6_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_2/2_6_1/',
        blank=True,
        null=True,
        help_text="Upload any additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide the link for additional information."
    )

    def save(self, *args, **kwargs):
        if Criteria_2_6_1.objects.exists():
            existing = Criteria_2_6_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link']
                )
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]
    
    
class Criteria_2_6_2(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_2/2_6_2/',
        blank=True,
        null=True,
        help_text="Upload any additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide the link for additional information."
    )

    def save(self, *args, **kwargs):
        if Criteria_2_6_2.objects.exists():
            existing = Criteria_2_6_2.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link']
                )
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]
    
class Criteria_2_6_3(models.Model):
    YEAR_CHOICES = [
        (2021, '2020-2021'),
        (2022, '2021-2022'),
        (2023, '2022-2023'),
        (2024, '2023-2024'),
        (2025, '2024-2025'),
    ]
    
    year = models.IntegerField(choices=YEAR_CHOICES)
    program_code = models.CharField(max_length=50)
    program_name = models.CharField(max_length=255)
    number_of_students_appeared = models.PositiveIntegerField()
    number_of_students_passed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.program_name} ({self.year})"
    
class Criteria_2_7_1(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.CharField(max_length=255)
    state_of_domicile = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255, default='Indian')
    email = models.EmailField()
    program_name = models.CharField(max_length=255)
    enrolment_id = models.CharField(max_length=255, unique=True)
    year_of_joining = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.program_name})"





