from django.db import models

# Create your models here.


class Criteria_7_1_1(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_7/7_1_1/',
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
        if Criteria_7_1_1.objects.exists():
            existing = Criteria_7_1_1.objects.first()
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


class Criteria_7_1_2(models.Model):
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
        existing_instance = Criteria_7_1_2.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()


class Criteria_7_1_3(models.Model):
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
        existing_instance = Criteria_7_1_3.objects.first()
        if existing_instance and existing_instance.pk != self.pk:
            existing_instance.selected_option = self.selected_option
            existing_instance.save(update_fields=['selected_option'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.get_selected_option_display()


class Criteria_7_1_4(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 500 words."
    )
    additional_information_file = models.FileField(
        upload_to='criteria_7/7_1_4/',
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
        if Criteria_7_1_4.objects.exists():
            existing = Criteria_7_1_4.objects.first()
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


class Criteria_7_3_1(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 1000 words."
    )
    weblink_to_institutional_website = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Appropriate web in the Institutional website."
    )
    weblink_to_other_relevant_info = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Link to other relevant information"
    )

    def save(self, *args, **kwargs):
        if Criteria_7_3_1.objects.exists():
            existing = Criteria_7_3_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.weblink_to_institutional_website = self.weblink_to_institutional_website
                existing.weblink_to_other_relevant_info = self.weblink_to_other_relevant_info
                existing.save(
                    update_fields=['description', 'weblink_to_institutional_website', 'weblink_to_other_relevant_info'])
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]


class Criteria_7_2_1(models.Model):
    description = models.TextField(
        help_text="Describe in a maximum of 1000 words."
    )
    weblink_to_institutional_website = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Best practices as hosted on the Institutional website."
    )
    weblink_to_other_relevant_info = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Any other relevant information"
    )

    def save(self, *args, **kwargs):
        if Criteria_7_2_1.objects.exists():
            existing = Criteria_7_2_1.objects.first()
            if existing.pk != self.pk:
                existing.description = self.description
                existing.weblink_to_institutional_website = self.weblink_to_institutional_website
                existing.weblink_to_other_relevant_info = self.weblink_to_other_relevant_info
                existing.save(
                    update_fields=['description', 'weblink_to_institutional_website', 'weblink_to_other_relevant_info'])
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description[:50]