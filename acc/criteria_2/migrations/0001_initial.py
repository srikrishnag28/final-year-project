# Generated by Django 5.0.7 on 2024-07-19 06:41

import criteria_2.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_2_1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, 'JUN-2021 - MAY-2022'), (2022, 'JUN-2022 - MAY-2023'), (2023, 'JUN-2023 - MAY-2024'), (2024, 'JUN-2024 - MAY-2025'), (2025, 'JUN-2025 - MAY-2026')])),
                ('programme_name', models.CharField(max_length=255)),
                ('programme_code', models.CharField(max_length=50)),
                ('number_of_seats_sanctioned', models.PositiveIntegerField()),
                ('number_of_students_admitted', models.PositiveIntegerField()),
                ('seats_earmarked_sc', models.PositiveIntegerField()),
                ('seats_earmarked_st', models.PositiveIntegerField()),
                ('seats_earmarked_obc', models.PositiveIntegerField()),
                ('seats_earmarked_gen', models.PositiveIntegerField()),
                ('seats_earmarked_others', models.PositiveIntegerField()),
                ('students_admitted_sc', models.PositiveIntegerField()),
                ('students_admitted_st', models.PositiveIntegerField()),
                ('students_admitted_obc', models.PositiveIntegerField()),
                ('students_admitted_gen', models.PositiveIntegerField()),
                ('students_admitted_others', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_1_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, 'JUN-2021 - MAY-2022'), (2022, 'JUN-2022 - MAY-2023'), (2023, 'JUN-2023 - MAY-2024'), (2024, 'JUN-2024 - MAY-2025'), (2025, 'JUN-2025 - MAY-2026')])),
                ('programme_name', models.CharField(max_length=255)),
                ('programme_code', models.CharField(max_length=50)),
                ('number_of_seats_sanctioned', models.PositiveIntegerField()),
                ('number_of_students_admitted', models.PositiveIntegerField()),
                ('seats_earmarked_sc', models.PositiveIntegerField()),
                ('seats_earmarked_st', models.PositiveIntegerField()),
                ('seats_earmarked_obc', models.PositiveIntegerField()),
                ('seats_earmarked_gen', models.PositiveIntegerField()),
                ('seats_earmarked_others', models.PositiveIntegerField()),
                ('students_admitted_sc', models.PositiveIntegerField()),
                ('students_admitted_st', models.PositiveIntegerField()),
                ('students_admitted_obc', models.PositiveIntegerField()),
                ('students_admitted_gen', models.PositiveIntegerField()),
                ('students_admitted_others', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_3_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2021-2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')])),
                ('description', models.TextField(validators=[criteria_2.models.validate_word_count])),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_5_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2021-2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')])),
                ('description', models.TextField(validators=[criteria_2.models.validate_word_count])),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_6_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2021-2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')])),
                ('description', models.TextField(validators=[criteria_2.models.validate_word_count])),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_6_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2021-2022'), (2022, '2022-2023'), (2023, '2023-2024'), (2024, '2024-2025'), (2025, '2025-2026')])),
                ('description', models.TextField(validators=[criteria_2.models.validate_word_count])),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_6_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2020-2021'), (2022, '2021-2022'), (2023, '2022-2023'), (2024, '2023-2024'), (2025, '2024-2025')])),
                ('program_code', models.CharField(max_length=50)),
                ('program_name', models.CharField(max_length=255)),
                ('number_of_students_appeared', models.PositiveIntegerField()),
                ('number_of_students_passed', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_7_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('category', models.CharField(max_length=255)),
                ('state_of_domicile', models.CharField(max_length=255)),
                ('nationality', models.CharField(default='Indian', max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('program_name', models.CharField(max_length=255)),
                ('enrolment_id', models.CharField(max_length=255, unique=True)),
                ('year_of_joining', models.IntegerField()),
            ],
        ),
    ]