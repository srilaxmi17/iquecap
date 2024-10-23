# razorpay_service.py
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_order(amount, currency='INR'):
    data = {
        'amount': amount,
        'currency': currency,
        'payment_capture': 1  # Auto capture payment after order creation
    }
    try:
        order = client.order.create(data=data)
        return order
    except Exception as e:
        print(f"Razorpay order creation failed: {str(e)}")
        return None


def capture_payment(order_id, amount):
    try:
        # Capture payment using order_id and amount
        payment = client.payment.capture(order_id, amount=amount)
        return payment
    except Exception as e:
        print(f"Razorpay payment capture failed: {str(e)}")
        return None
