# Generated by Django 4.2.1 on 2023-06-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_skill_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='startDate',
            field=models.DateField(),
        ),
    ]
