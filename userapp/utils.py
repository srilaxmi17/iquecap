from twilio.rest import Client
from django.conf import settings

def send_otp_via_twilio(mobile_number, otp):
    # Ensure the mobile number includes the country code
    if not mobile_number.startswith('+'):
        mobile_number = '+91' + mobile_number  # Assuming the country code for India

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=mobile_number
        )
        return message.sid
    except Exception as e:
        print(f"Error sending OTP: {e}")
        raise