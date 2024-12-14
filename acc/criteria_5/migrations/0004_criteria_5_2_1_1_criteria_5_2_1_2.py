# Generated by Django 5.0.7 on 2024-12-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_5', '0003_criteria_5_1_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_5_2_1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('student_name', models.CharField(max_length=255)),
                ('program_graduated_from', models.CharField(max_length=255)),
                ('year_of_graduation', models.IntegerField()),
                ('employer_name_with_contact', models.TextField()),
                ('pay_package_per_annum', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_5_2_1_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('student_name', models.CharField(max_length=255)),
                ('program_graduated_from', models.CharField(max_length=255)),
                ('year_of_graduation', models.IntegerField()),
                ('institution_joined', models.CharField(max_length=255)),
                ('program_admitted_to', models.CharField(max_length=255)),
            ],
        ),
    ]
