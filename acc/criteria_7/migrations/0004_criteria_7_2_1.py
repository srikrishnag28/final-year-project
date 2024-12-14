# Generated by Django 5.0.7 on 2024-12-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_7', '0003_criteria_7_3_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_7_2_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Describe in a maximum of 1000 words.')),
                ('weblink_to_institutional_website', models.URLField(blank=True, help_text='Best practices as hosted on the Institutional website.', max_length=500, null=True)),
                ('weblink_to_other_relevant_info', models.URLField(blank=True, help_text='Any other relevant information', max_length=500, null=True)),
            ],
        ),
    ]