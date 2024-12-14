# Generated by Django 5.0.7 on 2024-12-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria_5', '0002_criteria_5_4_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_5_1_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('guidance_activity_name', models.CharField(max_length=255)),
                ('guidance_students_participated', models.IntegerField()),
                ('guidance_students_qualified', models.IntegerField()),
                ('counselling_activity_name', models.CharField(max_length=255)),
                ('counselling_students_participated', models.IntegerField()),
                ('counselling_students_placed', models.IntegerField()),
            ],
        ),
    ]
