from django.db import models

# Create your models here.



class Criteria_5_1_1(models.Model):
    GOVERNMENT_CHOICES = [
        ('Government', 'Government'),
        ('Non-Government', 'Non-Government'),
    ]

    year = models.IntegerField()
    scheme_name = models.CharField(max_length=255)
    government_or_non_government = models.CharField(
        max_length=15,
        choices=GOVERNMENT_CHOICES,
    )
    individual_or_organization_name = models.CharField(max_length=255)
    number_of_students_benefited = models.IntegerField()
    amount_in_inr = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.scheme_name} ({self.year})"


class Criteria_5_1_2(models.Model):
    OPTION_CHOICES = [
        ('A', 'All of the above'),
        ('B', 'Any 3 of the above'),
        ('C', 'Any 2 of the above'),
        ('D', 'Any 1 of the above'),
        ('E', 'None of the above'),
    ]
    selected_option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICES,
        default='E'
    )

    def save(self, *args, **kwargs):
        existing_instance = Criteria_5_1_2.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()


class Criteria_5_1_3(models.Model):
    year = models.IntegerField()
    guidance_activity_name = models.CharField(max_length=255)
    guidance_students_participated = models.IntegerField()
    guidance_students_qualified = models.IntegerField()
    counselling_activity_name = models.CharField(max_length=255)
    counselling_students_participated = models.IntegerField()
    counselling_students_placed = models.IntegerField()
    def __str__(self):
        return f"Year: {self.year}, Guidance Activity: {self.guidance_activity_name}"


class Criteria_5_1_4(models.Model):
    OPTION_CHOICES = [
        ('A', 'All of the above'),
        ('B', 'Any 3 of the above'),
        ('C', 'Any 2 of the above'),
        ('D', 'Any 1 of the above'),
        ('E', 'None of the above'),
    ]
    selected_option = models.CharField(
        max_length=1,
        choices=OPTION_CHOICES,
        default='E'
    )

    def save(self, *args, **kwargs):
        existing_instance = Criteria_5_1_4.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()


class Criteria_5_2_1_1(models.Model):
    year = models.IntegerField()
    student_name = models.CharField(max_length=255)
    program_graduated_from = models.CharField(max_length=255)
    year_of_graduation = models.IntegerField()
    employer_name_with_contact = models.TextField()
    pay_package_per_annum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.student_name} - {self.year}"


class Criteria_5_2_1_2(models.Model):
    year = models.IntegerField()
    student_name = models.CharField(max_length=255)
    program_graduated_from = models.CharField(max_length=255)
    year_of_graduation = models.IntegerField()
    institution_joined = models.CharField(max_length=255)
    program_admitted_to = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student_name} - {self.year}"


class Criteria_5_2_2(models.Model):
    year = models.IntegerField()
    registration_or_roll_number = models.CharField(max_length=100, help_text="Enter the registration or roll number for the exam")
    student_name = models.CharField(max_length=255, help_text="Enter the name of the student qualified")
    qualifying_exam_name = models.CharField(max_length=255, help_text="Enter the name of the qualifying exam")

    def __str__(self):
        return f"{self.student_name} - {self.qualifying_exam_name} ({self.year})"


class Criteria_5_3_1(models.Model):
    year = models.IntegerField()
    name_of_award_medal = models.CharField(max_length=255)
    team_or_individual = models.CharField(max_length=50, choices=[('Team', 'Team'), ('Individual', 'Individual')])
    level_of_competition = models.CharField(max_length=50, choices=[
        ('University', 'University'),
        ('State', 'State'),
        ('National', 'National'),
        ('International', 'International')
    ])
    nature_of_competition = models.CharField(max_length=50, choices=[('Sports', 'Sports'), ('Cultural', 'Cultural')])
    name_of_students = models.TextField(help_text="Enter names separated by commas for team awards")

    def __str__(self):
        return f"Year: {self.year}, Award: {self.name_of_award_medal}"


class Criteria_5_3_2(models.Model):
    YEAR_CHOICES = [
        (2021, 'June 2021 - 2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES)
    date_of_event = models.DateField()
    name_of_event = models.CharField(max_length=255)
    name_of_organising_institution = models.CharField(max_length=255)
    name_of_student_participated = models.TextField(help_text="Enter names separated by commas")

    def __str__(self):
        return f"{self.year}: Event {self.name_of_event} on {self.date_of_event}"


class Criteria_5_4_1(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_5/5_4_1/',
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
        if Criteria_5_4_1.objects.exists():
            existing = Criteria_5_4_1.objects.first()
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