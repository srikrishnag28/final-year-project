# Generated by Django 5.0.7 on 2024-12-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_1', '0002_remove_criteria_1_1_1_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria_1_3_2',
            name='year',
        ),
        migrations.AlterField(
            model_name='criteria_1_3_2',
            name='document_link',
            field=models.URLField(blank=True, help_text='Provide the link to the relevant document.', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='criteria_1_3_2',
            name='programme_code',
            field=models.CharField(help_text='Enter the code of the programme.', max_length=100),
        ),
        migrations.AlterField(
            model_name='criteria_1_3_2',
            name='programme_name',
            field=models.CharField(help_text='Enter the name of the programme.', max_length=255),
        ),
        migrations.AlterField(
            model_name='criteria_1_3_2',
            name='student_list',
            field=models.TextField(help_text='List of students undertaking project work/field work/internship.'),
        ),
    ]
