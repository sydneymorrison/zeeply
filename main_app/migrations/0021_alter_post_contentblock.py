# Generated by Django 4.2.1 on 2023-06-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_alter_skill_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contentBlock',
            field=models.TextField(max_length=10000),
        ),
    ]
