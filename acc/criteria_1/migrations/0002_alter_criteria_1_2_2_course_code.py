# Generated by Django 5.0.7 on 2024-07-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria_1_2_2',
            name='course_code',
            field=models.CharField(max_length=50),
        ),
    ]
