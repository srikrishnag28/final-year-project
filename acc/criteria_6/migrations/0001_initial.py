# Generated by Django 5.0.7 on 2024-12-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_6_3_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('name_of_teacher', models.CharField(max_length=255)),
                ('name_of_conference_or_workshop', models.CharField(max_length=255)),
                ('name_of_professional_body', models.CharField(max_length=255)),
                ('amount_of_support_received_in_inr', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
