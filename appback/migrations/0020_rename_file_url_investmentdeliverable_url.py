# Generated by Django 5.0.2 on 2024-10-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0019_alter_investment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentdeliverable',
            old_name='file_url',
            new_name='url',
        ),
    ]
