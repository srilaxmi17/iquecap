from django.urls import path
# from .views import CreateRazorpayOrderView, payment_page
from . import views


urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('validate_payment/', views.validate_payment, name='validate_payment'),
    # path('create-order/', CreateRazorpayOrderView.as_view(), name='create_order'),
    # # path('verify-payment/', VerifyRazorpayPaymentView.as_view(), name='verify_payment'),
    # path('payment/<int:investment_id>/', payment_page, name='payment_page'),
]
