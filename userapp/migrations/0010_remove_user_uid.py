# Generated by Django 5.0.2 on 2024-10-02 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_user_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
    ]
