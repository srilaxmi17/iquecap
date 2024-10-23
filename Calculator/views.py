# calculator/views.py
from rest_framework import status,permissions
from rest_framework import generics
from .models import SIPCalculator
from .serializers import SIPCalculatorSerializer

# Create and List
class SIPCalculatorListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]

    queryset = SIPCalculator.objects.all()
    serializer_class = SIPCalculatorSerializer

# Retrieve, Update, and Delete
class SIPCalculatorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    
    queryset = SIPCalculator.objects.all()
    serializer_class = SIPCalculatorSerializer