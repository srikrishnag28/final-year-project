from django.db import models
from django.core.exceptions import ValidationError

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 500:
        raise ValidationError(f'Description cannot exceed 500 words. Current word count: {word_count}')

class Criteria_3_1_1(models.Model):
    name = "3_1_1"
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    project_name = models.CharField(max_length=255)
    principal_investigator = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    year_of_award = models.IntegerField()
    amount_sanctioned = models.DecimalField(max_digits=10, decimal_places=2)  # Amount in INR Lakhs
    duration = models.CharField(max_length=100)  # e.g., "1 year", "6 months"
    funding_agency = models.CharField(max_length=255)
    grant_type = models.CharField(
        max_length=50,
        choices=[('Government', 'Government'), ('Non-Government', 'Non-Government')]
    )

    def __str__(self):
        return f"{self.year} - {self.project_name})"

class Criteria_3_2_1(models.Model):
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    description = models.TextField(validators=[validate_word_count])

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"
    

class Criteria_3_2_2(models.Model):
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    event_name = models.CharField(max_length=255)
    num_participants = models.PositiveIntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    activity_report_link = models.URLField()

    def __str__(self):
        return f"{self.event_name} ({self.year})"
    

class Criteria_3_3_1(models.Model):
    year = models.PositiveIntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )  # Dedicated year field
    title_of_paper = models.CharField(max_length=255)
    authors = models.CharField(max_length=500)  # Considering multiple authors
    department = models.CharField(max_length=255)
    journal_name = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    issn_number = models.CharField(max_length=20, blank=True, null=True)  # ISSN number can be optional
    journal_website_link = models.URLField(blank=True, null=True)  # URL to the journal's website
    article_link = models.URLField(blank=True, null=True)  # URL to the article/paper/abstract
    is_ugc_care_listed = models.BooleanField(default=False)  # Boolean to indicate if listed in UGC CARE list

    def __str__(self):
        return f"{self.title_of_paper} ({self.year})"

class Criteria_3_3_2(models.Model):
    year = models.PositiveIntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    serial_number = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=255)
    book_or_chapter_title = models.CharField(max_length=255, blank=True, null=True)
    paper_title = models.CharField(max_length=255, blank=True, null=True)
    proceedings_title = models.CharField(max_length=255, blank=True, null=True)
    conference_name = models.CharField(max_length=255, blank=True, null=True)
    conference_type = models.CharField(
        max_length=20,
        choices=[('National', 'National'), ('International', 'International')],
    )
    publication_year = models.PositiveIntegerField()
    isbn_number = models.CharField(max_length=20, blank=True, null=True)
    affiliating_institute = models.CharField(max_length=255, blank=True, null=True)
    publisher_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.teacher_name} - {self.paper_title or self.book_or_chapter_title} ({self.publication_year})"

class Criteria_3_4_1(models.Model):
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    description = models.TextField(validators=[validate_word_count])

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"

class Criteria_3_4_2(models.Model):
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    description = models.TextField(validators=[validate_word_count])
    def __str__(self):
        return f"{self.year} - {self.description[:50]}"

class Criteria_3_4_3(models.Model):
    year = models.IntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    activity_name = models.CharField(max_length=255)
    organizing_unit = models.CharField(max_length=255) 
    scheme_name = models.CharField(max_length=255, blank=True, null=True)
    activity_year = models.PositiveIntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )

    def __str__(self):
        return f"{self.activity_name} ({self.activity_year})"

class Criteria_3_5_1(models.Model):
    year = models.PositiveIntegerField(
        choices=[(2021, '2021-2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),]
    )
    mou_name = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    signing_year = models.PositiveIntegerField()
    PURPOSE_CHOICES = [
        ('Internship', 'Internship'),
        ('On-the-job Training', 'On-the-job Training'),
        ('Project Work', 'Project Work'),
        ('Student/Faculty Exchange', 'Student/Faculty Exchange'),
        ('Collaborative Research', 'Collaborative Research'),
    ]
    pourpose = models.CharField(choices=PURPOSE_CHOICES, max_length=100)
    duration = models.CharField(max_length=100)
    activities = models.TextField()  
    document_link = models.URLField()

    def __str__(self):
        return f"{self.mou_name} ({self.signing_year})"
