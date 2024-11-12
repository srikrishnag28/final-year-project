from django.db import models
from django.core.exceptions import ValidationError
from user.models import CustomUser

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 500:
        raise ValidationError(f'Description cannot exceed 500 words. Current word count: {word_count}')

class Criteria_1_1_1(models.Model):
    year = models.IntegerField()
    description = models.TextField(validators=[validate_word_count])

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"
    
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
    year = models.IntegerField()
    description = models.TextField(validators=[validate_word_count])

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"
    
class Criteria_1_3_2(models.Model):
    year = models.IntegerField()
    programme_name = models.CharField(max_length=255)
    programme_code = models.CharField(max_length=50)
    student_list = models.TextField()  # Store a list of students, possibly as a comma-separated string or JSON
    document_link = models.URLField()

    def __str__(self):
        return f"{self.year} - {self.programme_name} ({self.programme_code})"