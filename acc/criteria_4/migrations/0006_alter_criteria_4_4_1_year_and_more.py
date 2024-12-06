# Generated by Django 5.0.7 on 2024-12-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_4', '0005_alter_criteria_4_1_1_additional_information_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria_4_4_1',
            name='year',
            field=models.IntegerField(choices=[(2021, 'June 2021 - 2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')]),
        ),
        migrations.AlterField(
            model_name='criteria_4_4_1_total',
            name='year',
            field=models.IntegerField(choices=[(2021, 'June 2021 - 2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')]),
        ),
    ]