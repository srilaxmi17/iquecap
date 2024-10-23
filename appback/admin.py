# admin.py

from django.contrib import admin
from appback.models import *


# class SlotInline(admin.TabularInline):
#     model = Slot
#     extra = 4  # Allow admin to add up to 4 slots per company

# class eqAPInline(admin.TabularInline):
#     model = eqAP

# class CompanyAdmin(admin.ModelAdmin):
#     inlines = [SlotInline]
#     inlines = [eqAPInline]

class SlotInline(admin.TabularInline):
    model = Slot
    extra = 4

class eqAPInline(admin.TabularInline):
    model = eqAP
    max_num = 1

class c_BenefitsInline(admin.TabularInline):
    model = c_Benefits

class c_fileurlsInline(admin.TabularInline):
    model = c_fileurls

class CompanyAdmin(admin.ModelAdmin):
    inlines = [eqAPInline, SlotInline,c_BenefitsInline,c_fileurlsInline]

# admin.site.register(Company, CompanyAdmin)
admin.site.register(InvestmentTerm)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Investment)
admin.site.register(InvestmentDeliverable)
admin.site.register(feeds)
admin.site.register(company_portfolio)
