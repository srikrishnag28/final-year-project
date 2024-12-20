# Generated by Django 5.0.7 on 2024-12-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_3_1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, 'June 2021 to May 2022'), (2022, 'June 2022 to May 2023'), (2023, 'June 2023 to May 2024'), (2024, 'June 2024 to May 2025'), (2025, 'June 2025 to May 2026')])),
                ('project_name', models.CharField(max_length=255)),
                ('principal_investigator', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('year_of_award', models.IntegerField()),
                ('amount_sanctioned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=100)),
                ('funding_agency', models.CharField(max_length=255)),
                ('grant_type', models.CharField(choices=[('Government', 'Government'), ('Non-Government', 'Non-Government')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_2_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Describe the adequacy of facilities in a maximum of 500 words.')),
                ('additional_information_file', models.FileField(blank=True, help_text='Upload additional information if available.', null=True, upload_to='criteria_3/3_2_1/')),
                ('additional_information_link', models.URLField(blank=True, help_text='Provide a link for additional information if available.', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_2_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, 'June 2021 to May 2022'), (2022, 'June 2022 to May 2023'), (2023, 'June 2023 to May 2024'), (2024, 'June 2024 to May 2025'), (2025, 'June 2025 to May 2026')])),
                ('event_name', models.CharField(max_length=255)),
                ('num_participants', models.PositiveIntegerField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('activity_report_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_3_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2020-2021'), (2022, '2021-2022'), (2023, '2022-2023'), (2024, '2023-2024'), (2025, '2024-2025')])),
                ('title_of_paper', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=255)),
                ('journal_name', models.CharField(max_length=255)),
                ('year_of_publication', models.IntegerField()),
                ('issn_number', models.CharField(blank=True, max_length=20, null=True)),
                ('journal_website_link', models.URLField(blank=True, null=True)),
                ('article_link', models.URLField(blank=True, null=True)),
                ('is_ugc_care_listed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_3_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_teacher', models.CharField(max_length=255)),
                ('title_of_book_or_chapters_published', models.CharField(blank=True, max_length=500, null=True)),
                ('title_of_paper', models.CharField(blank=True, max_length=500, null=True)),
                ('title_of_proceedings_of_conference', models.CharField(blank=True, max_length=500, null=True)),
                ('name_of_conference', models.CharField(blank=True, max_length=255, null=True)),
                ('national_or_international', models.CharField(blank=True, choices=[('National', 'National'), ('International', 'International')], max_length=50, null=True)),
                ('calendar_year_of_publication', models.IntegerField()),
                ('isbn_number_of_proceeding', models.CharField(blank=True, max_length=20, null=True)),
                ('affiliating_institute_at_time_of_publication', models.CharField(max_length=255)),
                ('name_of_publisher', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_4_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Describe the adequacy of facilities in a maximum of 500 words.')),
                ('additional_information_file', models.FileField(blank=True, help_text='Upload additional information if available.', null=True, upload_to='criteria_3/3_4_1/')),
                ('additional_information_link', models.URLField(blank=True, help_text='Provide a link for additional information if available.', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_4_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Describe the adequacy of facilities in a maximum of 500 words.')),
                ('additional_information_file', models.FileField(blank=True, help_text='Upload additional information if available.', null=True, upload_to='criteria_3/3_4_2/')),
                ('additional_information_link', models.URLField(blank=True, help_text='Provide a link for additional information if available.', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_4_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_activity', models.CharField(max_length=255)),
                ('organising_unit_or_agency_or_collaborating_agency', models.CharField(max_length=255)),
                ('name_of_scheme', models.CharField(max_length=255)),
                ('year_of_activity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_3_5_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, '2020-2021'), (2022, '2021-2022'), (2023, '2022-2023'), (2024, '2023-2024'), (2025, '2024-2025')])),
                ('mou_name', models.CharField(max_length=255)),
                ('institution_name', models.CharField(max_length=255)),
                ('signing_year', models.PositiveIntegerField()),
                ('pourpose', models.CharField(choices=[('Internship', 'Internship'), ('On-the-job Training', 'On-the-job Training'), ('Project Work', 'Project Work'), ('Student/Faculty Exchange', 'Student/Faculty Exchange'), ('Collaborative Research', 'Collaborative Research')], max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('activities', models.TextField()),
                ('document_link', models.URLField()),
            ],
        ),
    ]
