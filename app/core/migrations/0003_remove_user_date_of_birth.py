# Generated by Django 3.2.13 on 2022-06-20 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]
