import razorpay
import uuid
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status,permissions
from django.conf import settings

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

@api_view(['POST'])
@permission_classes([AllowAny])
def create_order(request):
    """
    Endpoint to create a new order with Razorpay.
    Expects amount in the request data.
    """
    amount = request.data.get('amount')

    if not amount:
        return Response({'error': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount = float(amount)
        if amount <= 0:
            return Response({'error': 'Amount must be greater than zero'}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a unique order ID
    order_id = str(uuid.uuid4())

    try:
        # Create an order in Razorpay
        razorpay_order = client.order.create({
            'amount': int(amount * 100),  # Razorpay expects amount in paise
            'currency': 'INR',
            'receipt': order_id
        })
        return Response({'order_id': razorpay_order['id']}, status=status.HTTP_201_CREATED)
    except razorpay.errors.RazorpayError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def validate_payment(request):
    """
    Endpoint to verify a payment with Razorpay.
    Expects razorpay_payment_id, razorpay_order_id, and razorpay_signature in the request data.
    """
    payment_id = request.data.get('razorpay_payment_id')
    order_id = request.data.get('razorpay_order_id')
    signature = request.data.get('razorpay_signature')

    if not all([payment_id, order_id, signature]):
        return Response({'error': 'Payment ID, Order ID, and Signature are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Verify payment signature
        client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        })

        # Here you can update your backend with the payment status
        # For example, mark the order as paid

        return Response({'status': 'Payment verified successfully'}, status=status.HTTP_200_OK)

    except razorpay.errors.SignatureVerificationError:
        return Response({'error': 'Signature verification failed'}, status=status.HTTP_400_BAD_REQUEST)