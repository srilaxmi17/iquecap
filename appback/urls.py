# invest/urls.py
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from appback.views import *

urlpatterns = [
    path('investments/', InvestmentTermList.as_view(), name='investment-term-list'),
    path('investments/<int:id>/', InvestmentTermidList.as_view(), name='investment-term-id-list'),
    path('investments/<int:investment_term_id>/companies/', InvestmentTermCompany.as_view(), name='investment-term-company'),
    path('investments/<int:investment_term_id>/companies/<int:company_id>/', InvestmentTermCompanyid.as_view(), name='investment-term-company-id'),
    path('investments/place_order/', PortfolioCreateView.as_view(), name='investment-term-company-id-place-order'),
    path('portfolio/<int:user_id>/', DisplayPortfolio.as_view(), name='portfolio-user_id'),
    path('feeds/', feedlist.as_view(), name='feed-list'),



    path('companies/', CompanyList.as_view(), name='company-list'),
    path('fococompanies/', FocoCompanyList.as_view(), name='fococompany-list'),
    path('equitycompanies/', EquityCompanyList.as_view(), name='equitycompany-list'),
    path('slots/', SlotList.as_view(), name='slot-list'),
    # path('investments/', InvestmentCreate.as_view(), name='investment-create'),
    # path('investment-summary/', InvestmentSummaryView.as_view(), name='investment_summary'),


    path('news/', NewsListCreateAPIView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
]

