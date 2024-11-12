# Generated by Django 5.0.7 on 2024-10-22 08:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_criterialink'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCriteriaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(choices=[('3_1_1', 'Criteria 3.1.1'), ('3_2_2', 'Criteria 3.2.2'), ('3_3_1', 'Criteria 3.3.1'), ('3_5_1', 'Criteria 3.5.1')], max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CriteriaLink',
        ),
    ]
