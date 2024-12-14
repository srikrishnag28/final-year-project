from django.db import models

# Create your models here.


class Criteria_6_1_1(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_6/6_1_1/',
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
        if Criteria_6_1_1.objects.exists():
            existing = Criteria_6_1_1.objects.first()
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


class Criteria_6_2_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_6/6_2_1/',
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
        if Criteria_6_2_1.objects.exists():
            existing = Criteria_6_2_1.objects.first()
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


class Criteria_6_2_2(models.Model):
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
        existing_instance = Criteria_6_2_2.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()


class Criteria_6_3_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_6/6_3_1/',
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
        if Criteria_6_3_1.objects.exists():
            existing = Criteria_6_3_1.objects.first()
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


class Criteria_6_3_2(models.Model):
    year = models.IntegerField()
    name_of_teacher = models.CharField(max_length=255)
    name_of_conference_or_workshop = models.CharField(max_length=255)
    name_of_professional_body = models.CharField(max_length=255)
    amount_of_support_received_in_inr = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name_of_conference_or_workshop} ({self.year}) - {self.name_of_teacher}"


class Criteria_6_3_3(models.Model):
    year = models.IntegerField()
    name_of_participant = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    title_of_program = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"{self.title_of_program} ({self.year}) - {self.name_of_participant}"
    

class Criteria_6_4_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_6/6_4_1/',
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
        if Criteria_6_4_1.objects.exists():
            existing = Criteria_6_4_1.objects.first()
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
    

class Criteria_6_5_1(models.Model):
    description = models.TextField(
        help_text="Write the description in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_6/6_5_1/',
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
        if Criteria_6_5_1.objects.exists():
            existing = Criteria_6_5_1.objects.first()
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


class Criteria_6_5_2(models.Model):
    OPTION_CHOICES = [
        ('A', 'Any 4 or more of the above'),
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
        existing_instance = Criteria_6_5_2.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()