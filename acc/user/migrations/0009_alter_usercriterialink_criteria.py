# Generated by Django 5.0.7 on 2024-12-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_usercriterialink_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercriterialink',
            name='criteria',
            field=models.CharField(choices=[('1_1_1', 'Criteria 1.1.1'), ('1_2_2', 'Criteria 1.2.2'), ('1_3_1', 'Criteria 1.3.1'), ('1_3_2', 'Criteria 1.3.2'), ('2_3_1', 'Criteria 2.3.1'), ('2_5_1', 'Criteria 2.5.1'), ('2_6_1', 'Criteria 2.6.1'), ('2_6_2', 'Criteria 2.6.2'), ('2_6_3', 'Criteria 2.6.3'), ('2_7_1', 'Criteria 2.7.1'), ('3_1_1', 'Criteria 3.1.1'), ('3_2_1', 'Criteria 3.2.1'), ('3_2_2', 'Criteria 3.2.2'), ('3_3_1', 'Criteria 3.3.1'), ('3_4_1', 'Criteria 3.4.1'), ('3_4_2', 'Criteria 3.4.2'), ('3_5_1', 'Criteria 3.5.1'), ('4_1_1', 'Criteria 4.1.1'), ('4_1_2', 'Criteria 4.1.2'), ('4_2_1', 'Criteria 4.2.1'), ('4_3_1', 'Criteria 4.3.1'), ('4_4_1', 'Criteria 4.4.1'), ('5_1_1', 'Criteria 5.1.1'), ('5_1_2', 'Criteria 5.1.2'), ('5_1_3', 'Criteria 5.1.3'), ('5_1_4', 'Criteria 5.1.4'), ('5_2_1', 'Criteria 5.2.1'), ('5_2_2', 'Criteria 5.2.2'), ('5_3_1', 'Criteria 5.3.1'), ('5_3_2', 'Criteria 5.3.2'), ('5_4_1', 'Criteria 5.4.1'), ('6_1_1', 'Criteria 6.1.1'), ('6_2_1', 'Criteria 6.2.1'), ('6_2_2', 'Criteria 6.2.2'), ('6_3_1', 'Criteria 6.3.1'), ('6_3_2', 'Criteria 6.3.2'), ('6_3_3', 'Criteria 6.3.3'), ('6_4_1', 'Criteria 6.4.1'), ('6_5_1', 'Criteria 6.5.1'), ('6_5_2', 'Criteria 6.5.2'), ('7_1_1', 'Criteria 7.1.1'), ('7_1_2', 'Criteria 7.1.2'), ('7_1_3', 'Criteria 7.1.3'), ('7_1_4', 'Criteria 7.1.4'), ('7_2_1', 'Criteria 7.2.1'), ('7_3_1', 'Criteria 7.3.1')], max_length=10),
        ),
    ]
