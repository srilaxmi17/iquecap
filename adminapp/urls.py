from django.urls import path
from adminapp import views
from adminapp.views import block_user, unblock_user,investment_list

app_name = 'adminapp'


urlpatterns = [
    path('add_company/', views.add_company, name='add_company'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/edit/<int:company_id>/', views.edit_company, name='edit_company'),
    path('companies/delete/<int:company_id>/', views.delete_company, name='delete_company'),
    path('index', views.index, name='index'),
    path('add_investment_term/', views.add_investment_term, name='add_investment_term'),
    path('investment_term_list/', views.investment_terms_list, name='investment_term_list'),
    path('terms/edit/<int:term_id>/', views.edit_investment_term, name='edit_investment_term'),
    path('terms/delete/<int:term_id>/', views.delete_investment_term, name='delete_investment_term'),
    path('investment_list/', views.investment_list, name='investment_list'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('news/add/', views.add_news, name='add_news'),
    path('news/', views.news_list, name='news_list'),
    path('news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
