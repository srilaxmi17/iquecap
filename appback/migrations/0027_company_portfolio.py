# Generated by Django 5.0.2 on 2024-10-06 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0026_slot_slot_type'),
        ('userapp', '0014_remove_user_groups_remove_user_last_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appback.company')),
                ('investment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appback.investmentterm')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appback.slot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
