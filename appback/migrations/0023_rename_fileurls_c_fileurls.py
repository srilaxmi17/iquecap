# Generated by Django 5.0.2 on 2024-10-05 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0022_rename_subscription_model_company_business_stage_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fileurls',
            new_name='c_fileurls',
        ),
    ]
