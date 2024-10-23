from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from rest_framework.exceptions import NotFound
from userapp.serializers import *
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView
from datetime import timedelta
from .utils import send_otp_via_twilio
from rest_framework.permissions import IsAuthenticated
import re 
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# class CustomTokenRefreshView(BaseTokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Custom logic before token refresh, if needed
#             refresh = serializer.validated_data.get('refresh')
#             new_access_token = serializer.get_token(refresh)

#             # Custom response data example
#             return Response({
#                 'access': str(new_access_token.access_token),
#                 'expires_at': str(new_access_token.access_token.payload['exp']),
#                 'token_type': 'Bearer',
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]

#     @action(detail=False, methods=['delete'], permission_classes=[permissions.AllowAny])
#     def delete_user_by_mobile(self, request):
#         mobile_number = request.data.get('mobile_number', None)
        
#         if not mobile_number:
#             return Response({'error': 'Mobile number must be provided'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = User.objects.get(mobile_number=mobile_number)
#         except User.DoesNotExist:
#             return Response({'error': 'User with this mobile number does not exist'}, status=status.HTTP_404_NOT_FOUND)

#         user.delete()
#         return Response({'message': f'User with mobile number {mobile_number} has been deleted'}, status=status.HTTP_200_OK)

    
#     @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
#     def logout(self, request):
#         serializer = LogoutSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
#     def update_profile(self, request):
#         print(f"Authenticated user: {request.user}")
        
#         user = request.user
#         if not user.is_authenticated:
#             return Response({'detail': 'Authentication credentials were not provided or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        
#         serializer = UserSerializer(user, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 
#     @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
#     def view_profile(self, request):
#         user = request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
#     def put_update_profile(self, request):
#         user = request.user
#         print(f"Authenticated user: {request.user}")
        
#         serializer = UserSerializer(user, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

#     @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
#     def delete_profile(self, request):
#         user = request.user

#         try:
#             user.delete()
#             return Response({"message": "User profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    


# class RegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(
#                 {
#                     "message": "Successfully registered.",
#                     "mobile_number": user.mobile_number
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {
#                     "message": "Successfully logged in.",
#                     "mobile_number": user.mobile_number,
#                     "tokens": {
#                         "refresh": str(refresh),
#                         "access": str(refresh.access_token),
#                     }
#                 },
#                 status=status.HTTP_200_OK
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ChangeMobileNumberView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ChangeMobileNumberSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save(user=request.user)
#             return Response(
#                 {
#                     "message": "Mobile number updated successfully.",
#                     "mobile_number": user.mobile_number
#                 },
#                 status=status.HTTP_200_OK
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DeleteProfileView(APIView):
    permission_classes=[permissions.AllowAny]
    def delete(self, request, uid, *args, **kwargs):
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)




class CreateProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uid, *args, **kwargs):
        data = request.data.copy()
        data['uid'] = uid

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, uid, *args, **kwargs):
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Pass the existing instance (user) to the serializer, indicating an update operation
        serializer = UserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, *args, **kwargs):
        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)