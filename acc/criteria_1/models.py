from django.db import models
from django.core.exceptions import ValidationError
from user.models import CustomUser

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 500:
        raise ValidationError(f'Description cannot exceed 500 words. Current word count: {word_count}')

class Criteria_1_1_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_1/1_1_1/',
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
        if Criteria_1_1_1.objects.exists():
            existing = Criteria_1_1_1.objects.first()
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
    
class Criteria_1_2_1(models.Model):
    num=models.IntegerField()

    def __str__(self):
        return self.num
    
class Criteria_1_2_2(models.Model):
    YEAR_CHOICES = [
        (2021, 'June 2021 - 2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50) 
    year_of_study = models.IntegerField()
    period_from = models.DateField()
    period_to = models.DateField()
    duration = models.CharField(max_length=100)
    students_enrolled = models.IntegerField()
    students_completed = models.IntegerField()

    def __str__(self):
        return f"{self.course_name}"
    
class Criteria_1_3_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_1/1_3_1/',
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
        if Criteria_1_3_1.objects.exists():
            existing = Criteria_1_3_1.objects.first()
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


class Criteria_1_3_2(models.Model):
    programme_name = models.CharField(
        max_length=255,
        help_text="Enter the name of the programme."
    )
    programme_code = models.CharField(
        max_length=100,
        help_text="Enter the code of the programme."
    )
    student_list = models.TextField(
        help_text="List of students undertaking project work/field work/internship."
    )
    document_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide the link to the relevant document."
    )

    def __str__(self):
        return f"{self.programme_name} ({self.programme_code})"
