# Generated by Django 5.0.2 on 2024-10-04 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_alter_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]