# Generated by Django 5.0.7 on 2024-12-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usercriterialink_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercriterialink',
            name='criteria',
            field=models.CharField(choices=[('2_7_1', 'Criteria 2.7.1'), ('2_6_3', 'Criteria 2.6.3'), ('3_1_1', 'Criteria 3.1.1'), ('3_2_2', 'Criteria 3.2.2'), ('3_3_1', 'Criteria 3.3.1'), ('3_5_1', 'Criteria 3.5.1'), ('4_1_1', 'Criteria 4.1.1'), ('4_1_2', 'Criteria 4.1.2'), ('4_2_1', 'Criteria 4.2.1'), ('4_3_1', 'Criteria 4.3.1'), ('4_3_2', 'Criteria 4.3.2'), ('4_4_1', 'Criteria 4.4.1')], max_length=10),
        ),
    ]
