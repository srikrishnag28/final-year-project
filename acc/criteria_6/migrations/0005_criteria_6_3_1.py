# Generated by Django 5.0.7 on 2024-12-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_6', '0004_criteria_6_2_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_6_3_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Write the description in a maximum of 500 words.')),
                ('additional_information_file', models.FileField(blank=True, help_text='Upload any additional information if available.', null=True, upload_to='criteria_6/6_3_1/')),
                ('additional_information_link', models.URLField(blank=True, help_text='Provide the link for additional information.', max_length=500, null=True)),
            ],
        ),
    ]
