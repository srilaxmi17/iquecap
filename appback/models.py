# models.py

from django.db import models
from django.contrib.auth.models import User
from userapp.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password


class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class InvestmentTerm(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    returns = models.CharField(max_length=255)
    deliverables = models.CharField(max_length=255)
    video=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title

class InvestmentDeliverable(models.Model):
    investment_term = models.ForeignKey(InvestmentTerm, related_name='deliverable', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title



class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField()
    bussiness_model = models.CharField(max_length=255)
    revenue_model = models.CharField(max_length=255,null=True,blank=True)
    industry = models.CharField(max_length=255,null=True,blank=True)
    duration = models.CharField(max_length=255)
    business_stage = models.CharField(max_length=255)
    hq = models.CharField(max_length=255,null=True,blank=True)
    year_founded=models.IntegerField(null=True,blank=True)
    percentage = models.CharField(max_length=255)
    investment_term = models.ForeignKey(InvestmentTerm, related_name='companies', on_delete=models.CASCADE)
    brochureUrl=models.URLField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class c_Benefits(models.Model):
    company=models.ForeignKey(Company, related_name='benefits', on_delete=models.CASCADE)
    benefits=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company}"
    
class c_fileurls(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)    
    c_f_title=models.CharField(max_length=255)
    c_f_urls=models.URLField(max_length=255)

    def __str__(self):
        return f"{self.company}"

class Slot(models.Model):
    investment_term = models.ForeignKey(InvestmentTerm, related_name='slots', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='slots', on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    fixed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    filled = models.BooleanField(default=False)
    slot_type=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.company.name} - {self.percentage}% - ${self.fixed_amount}"


class eqAP(models.Model):
    investment_term = models.ForeignKey(InvestmentTerm, related_name='eqAP', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='eqAP', on_delete=models.CASCADE)
    e_amount = models.IntegerField()
    e_percentage = models.IntegerField()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_term = models.ForeignKey(InvestmentTerm, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)  # Field to mark if the investment is paid


    def __str__(self):
        return f"{self.user.name} - {self.investment_term.title}"




    
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class feeds(models.Model):
    v_title=models.CharField(max_length=225)
    v_description=models.TextField()
    v_url=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.v_title
    

class company_portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    timestamp=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE,null=True,blank=True)
    investment_type=models.ForeignKey(InvestmentTerm,on_delete=models.CASCADE)