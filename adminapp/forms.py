
from django import forms
from django.forms import ModelForm
from appback.models import InvestmentTerm,Company,News

class InvestmentTermForm(forms.ModelForm):
    class Meta:
        model = InvestmentTerm
        fields = ['title', 'description', 'minimum_investment', 'duration', 'returns', 'deliverables', 'term_type']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'subscription_model', 'type', 'duration', 'percentage', 'logo', 'investment_term']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image']