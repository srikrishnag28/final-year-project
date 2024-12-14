# Generated by Django 5.0.7 on 2024-12-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_2', '0003_alter_criteria_2_3_1_additional_information_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_2_4_2_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=50)),
                ('vidwan_id', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('designation', models.CharField(max_length=255)),
                ('date_of_joining_institution', models.DateField()),
                ('nature_of_appointment', models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50)),
                ('department_name', models.CharField(max_length=255)),
                ('highest_qualification', models.CharField(max_length=255)),
                ('year_of_obtaining_qualification', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria_2_4_2_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_number', models.CharField(blank=True, max_length=50, null=True)),
                ('vidwan_id', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('designation', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('nature_of_appointment', models.CharField(choices=[('Against Sanctioned Post', 'Against Sanctioned Post'), ('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50)),
                ('department_name', models.CharField(max_length=255)),
                ('highest_qualification', models.CharField(max_length=255)),
                ('year_of_obtaining_qualification', models.IntegerField()),
            ],
        ),
    ]
