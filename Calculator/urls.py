from django.urls import path
from .views import SIPCalculatorListCreate, SIPCalculatorRetrieveUpdateDestroy

urlpatterns = [
    path('sip_calculators/', SIPCalculatorListCreate.as_view(), name='sip_calculator_list_create'),
    path('sip_calculators/<int:pk>/', SIPCalculatorRetrieveUpdateDestroy.as_view(), name='sip_calculator_detail'),
]