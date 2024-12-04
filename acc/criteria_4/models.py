from django.db import models


class Criteria_4_1_2(models.Model):
    YEAR_CHOICES = [
        (2021, 'June 2021 - 2022'),
        (2022, '2022-2023'),
        (2023, '2023-2024'),
        (2024, '2024-2025'),
        (2025, '2025-2026'),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    head_of_expenditure = models.CharField(max_length=255, help_text="e.g., Capital Expenditure")
    item_of_expenditure = models.CharField(
        max_length=255, help_text="e.g., Construction of building, purchase of equipment, etc."
    )
    amount_in_lakhs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Year {self.year} - {self.head_of_expenditure}: {self.amount_in_lakhs} Lakhs"


class Criteria_4_1_2_Total(models.Model):
    year = models.IntegerField(choices=Criteria_4_1_2.YEAR_CHOICES)
    total_amount_in_lakhs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Total for Year {self.year}: {self.total_amount_in_lakhs} Lakhs"


class Criteria_4_4_1(models.Model):
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
        (5, 'Year 5'),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    head_of_expenditure = models.CharField(max_length=255, help_text="e.g., Repair and Maintenance")
    item_of_expenditure = models.CharField(
        max_length=255, help_text="e.g., AMC for Lab equipment, garden maintenance, etc."
    )
    amount_in_lakhs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Year {self.year} - {self.head_of_expenditure}: {self.amount_in_lakhs} Lakhs"

class Criteria_4_4_1_Total(models.Model):
    year = models.IntegerField(choices=Criteria_4_4_1.YEAR_CHOICES)
    total_amount_in_lakhs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Total for Year {self.year}: {self.total_amount_in_lakhs} Lakhs"


class Criteria_4_1_1(models.Model):
    description = models.TextField(
        help_text="Describe the adequacy of facilities in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_4_1_1/', 
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

    def __str__(self):
        return self.description[:50]


class Criteria_4_2_1(models.Model):
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
        (5, 'Year 5'),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    description = models.TextField(
        help_text="Describe the library's digital facilities, automation, and usage in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_4_2_1/', 
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

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"

from django.db import models

class Criteria_4_3_1(models.Model):
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
        (5, 'Year 5'),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    description = models.TextField(
        help_text="Describe IT facilities, including Wi-Fi, updates (with dates and nature of updates), and internet bandwidth within a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_4_3_1/', 
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

    def __str__(self):
        return f"{self.year} - {self.description[:50]}"

class Criteria_4_3_2(models.Model):
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
        (5, 'Year 5'),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    number_of_students = models.IntegerField(help_text="Total number of students during the latest completed academic year")
    number_of_computers = models.IntegerField(help_text="Number of computers available for student usage during the latest completed academic year")
    supporting_document = models.FileField(
        upload_to='criteria_4_3_2/', 
        blank=True, 
        null=True, 
        help_text="Upload supporting documents if available."
    )
    additional_information_link = models.URLField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="Provide links for any other relevant documents to support the claim."
    )

    def __str__(self):
        return f"Year {self.year}: {self.number_of_students} students, {self.number_of_computers} computers"

