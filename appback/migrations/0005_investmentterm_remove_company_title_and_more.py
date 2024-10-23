# Generated by Django 5.0.2 on 2024-06-29 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0004_news'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('minimum_investment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=255)),
                ('returns', models.CharField(max_length=255)),
                ('deliverables', models.CharField(max_length=255)),
                ('term_type', models.CharField(choices=[('foco', 'FOCO'), ('equity', 'Equity'), ('short', 'Short Term'), ('long', 'Long Term')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='title',
        ),
        migrations.RemoveField(
            model_name='company',
            name='Company_name',
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appback.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('investment_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appback.investmentterm')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fixed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='appback.company')),
                ('investment_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='appback.investmentterm')),
            ],
        ),
        migrations.DeleteModel(
            name='Types_of_invest_details',
        ),
        migrations.DeleteModel(
            name='Types_of_invest',
        ),
    ]
