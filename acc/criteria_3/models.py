from django.db import models
from django.core.exceptions import ValidationError

def validate_word_count(value):
    word_count = len(value.split())
    if word_count > 500:
        raise ValidationError(f'Description cannot exceed 500 words. Current word count: {word_count}')

class Criteria_3_1_1(models.Model):
    name = "3_1_1"
    YEAR_CHOICES = [
        (2021, 'June 2021 to May 2022'),
        (2022, 'June 2022 to May 2023'),
        (2023, 'June 2023 to May 2024'),
        (2024, 'June 2024 to May 2025'),
        (2025, 'June 2025 to May 2026'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
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
    description = models.TextField(
        help_text="Describe the adequacy of facilities in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_3/3_2_1/',
        blank=True,
        null=True,
        help_text="Upload additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide a link for additional information if available."
    )

    def save(self, *args, **kwargs):
        if Criteria_3_2_1.objects.exists():
            existing = Criteria_3_2_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link'])
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]
    

class Criteria_3_2_2(models.Model):
    YEAR_CHOICES = [
        (2021, 'June 2021 to May 2022'),
        (2022, 'June 2022 to May 2023'),
        (2023, 'June 2023 to May 2024'),
        (2024, 'June 2024 to May 2025'),
        (2025, 'June 2025 to May 2026'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=255)
    num_participants = models.PositiveIntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    activity_report_link = models.URLField()

    def __str__(self):
        return f"{self.event_name} ({self.year})"
    

class Criteria_3_3_1(models.Model):
    YEAR_CHOICES = [
        (2021, '2020-2021'),
        (2022, '2021-2022'),
        (2023, '2022-2023'),
        (2024, '2023-2024'),
        (2025, '2024-2025'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
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
    name_of_teacher = models.CharField(max_length=255)
    title_of_book_or_chapters_published = models.CharField(max_length=500, blank=True, null=True)
    title_of_paper = models.CharField(max_length=500, blank=True, null=True)
    title_of_proceedings_of_conference = models.CharField(max_length=500, blank=True, null=True)
    name_of_conference = models.CharField(max_length=255, blank=True, null=True)
    national_or_international = models.CharField(max_length=50, choices=[('National', 'National'), ('International', 'International')], blank=True, null=True)
    calendar_year_of_publication = models.IntegerField()
    isbn_number_of_proceeding = models.CharField(max_length=20, blank=True, null=True)
    affiliating_institute_at_time_of_publication = models.CharField(max_length=255)
    name_of_publisher = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name_of_teacher}"


class Criteria_3_4_1(models.Model):
    description = models.TextField(
        help_text="Describe the adequacy of facilities in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_3/3_4_1/',
        blank=True,
        null=True,
        help_text="Upload additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide a link for additional information if available."
    )

    def save(self, *args, **kwargs):
        if Criteria_3_4_1.objects.exists():
            existing = Criteria_3_4_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link'])
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]


class Criteria_3_4_2(models.Model):
    description = models.TextField(
        help_text="Describe the adequacy of facilities in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_3/3_4_2/',
        blank=True,
        null=True,
        help_text="Upload additional information if available."
    )
    additional_information_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Provide a link for additional information if available."
    )

    def save(self, *args, **kwargs):
        if Criteria_3_4_2.objects.exists():
            existing = Criteria_3_4_2.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.additional_information_file = self.additional_information_file
                existing.additional_information_link = self.additional_information_link
                existing.save(
                    update_fields=['description', 'additional_information_file', 'additional_information_link'])
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]


class Criteria_3_4_3(models.Model):
    name_of_activity = models.CharField(max_length=255)
    organising_unit_or_agency_or_collaborating_agency = models.CharField(max_length=255)
    name_of_scheme = models.CharField(max_length=255)
    year_of_activity = models.IntegerField()

    def __str__(self):
        return f"{self.name_of_activity} ({self.year_of_activity})"


class Criteria_3_5_1(models.Model):
    YEAR_CHOICES = [
        (2021, '2020-2021'),
        (2022, '2021-2022'),
        (2023, '2022-2023'),
        (2024, '2023-2024'),
        (2025, '2024-2025'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
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
