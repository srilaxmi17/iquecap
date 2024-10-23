from rest_framework import status,permissions
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from appback.models import *
from rest_framework.permissions import IsAuthenticated
from appback.serializers import *
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
# RetrieveAPIView
# edit
class InvestmentTermList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = InvestmentTerm.objects.all()
    serializer_class = InvestmentTermSerializer

class InvestmentTermidList(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny]
    queryset= InvestmentTerm.objects.all()
    serializer_class=InvestmentTermidSerilaizer
    lookup_field = 'id'

class InvestmentTermCompany(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=InvestmentTermCompanySerializer
    def get_queryset(self):
        investment_term_id = self.kwargs['investment_term_id']
        return Company.objects.filter(investment_term=InvestmentTerm.objects.get(id=investment_term_id))
        # return Company.objects.filter(investment_term_id=investment_term_id)

class InvestmentTermCompanyid(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=InvestmentTermCompanyidSerializer
    def get_object(self):
        investment_term_id = self.kwargs['investment_term_id']
        company_id = self.kwargs['company_id']
        return get_object_or_404(Company.objects.filter(id=company_id,investment_term=InvestmentTerm.objects.get(id=investment_term_id)))
    
class feedlist(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    queryset=feeds.objects.all()
    serializer_class=feedSerializer

class PortfolioCreateView(GenericAPIView):
    permission_classes = [permissions.AllowAny]  # Adjust permission as needed
    serializer_class = PortfolioCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract validated data
        validated_data = serializer.validated_data
        user_id = validated_data['user_id']
        transaction_id = validated_data['transaction_id']
        amount = validated_data['amount']
        timestamp = validated_data.get('timestamp', None)
        investment_type_id = validated_data['investment_type']

        # Fetch user and investment type
        user = User.objects.get(id=user_id)
        investment_type = InvestmentTerm.objects.get(id=investment_type_id)

        # Fetch company and slot only if IDs are provided
        company = Company.objects.get(id=validated_data.get('company_id')) if validated_data.get('company_id') else None
        slot = Slot.objects.get(id=validated_data.get('slot_id')) if validated_data.get('slot_id') else None

        # Autogenerate timestamp if not provided
        if not timestamp:
            timestamp = timezone.now()

        # Create portfolio record
        portfolio = company_portfolio.objects.create(
            user=user,
            amount=amount,
            timestamp=timestamp,
            company=company,
            slot=slot,
            investment_type=investment_type,
        )

        # Response data
        response_data = {
            "user_id": user.id,
            "user_name": user.name,
            "company_id": company.id if company else None,
            "slot_id": slot.id if slot else None,
            # "slot_type": validated_data.get('slot_type', None),
            "slot_type":slot.slot_type if slot else None,
            "amount": str(amount),
            "investment_type": investment_type.title,  # Or use ID if needed
            "timestamp": timestamp.isoformat(),
            "transaction_id": transaction_id
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
class DisplayPortfolio(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListPortfolioSerializer
    lookup_field = 'user_id' 
    def get_queryset(self):
        user_id=self.kwargs['user_id']
        return company_portfolio.objects.filter(user=user_id)



# end

class CompanyList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SlotList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

# class InvestmentCreate(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Investment.objects.all()
#     serializer_class = InvestmentSerializer

#     def perform_create(self, serializer):
#         investment_term = serializer.validated_data['investment_term']
#         company = serializer.validated_data.get('company')
#         slot_id = self.request.data.get('slot')
#         amount = serializer.validated_data['amount']
#         user = self.request.user

#         if investment_term.id == 4:
#             if not company:
#                 raise ValidationError("Company must be selected for FOCO terms.")
            
#             # Check if the user has already invested in a slot for this term
#             if Investment.objects.filter(user=user, investment_term=investment_term).exists():
#                 raise ValidationError("You cannot invest in more than one slot for a FOCO term.")

#             try:
#                 slot = Slot.objects.get(id=slot_id, investment_term=investment_term, company=company)
#             except Slot.DoesNotExist:
#                 raise ValidationError("Invalid slot selected.")

#             if slot.filled:
#                 raise ValidationError("This slot is already filled.")

#             if amount != slot.fixed_amount:
#                 raise ValidationError("The amount must match the selected slot's fixed amount.")

#             # Mark the slot as filled
#             slot.filled = True
#             slot.save()
        
#         serializer.save(user=user)

# class InvestmentSummaryView(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = InvestmentSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Investment.objects.filter(user=user)
        
#         # Optionally, you can annotate each investment with the total invested amount
#         # queryset = queryset.annotate(total_invested_amount=Sum('amount'))

#         return queryset

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         total_invested_amount = queryset.aggregate(Sum('amount'))['amount__sum'] or 0
        
#         # Serialize the queryset
#         serializer = self.get_serializer(queryset, many=True)
        
#         # Create a response dictionary
#         response_data = {
#             'total_invested_amount': total_invested_amount,
#             'investments': serializer.data
#         }
        
#         return Response(response_data)





class NewsListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer




class FocoCompanyList(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=CompanySerializer
    try:
        foco_term=InvestmentTerm.objects.get(id=1)
        queryset=Company.objects.filter(investment_term=foco_term)
    except ObjectDoesNotExist:
        queryset=Company.objects.none()


class EquityCompanyList(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=EquityComSerializer
    # equity_term=InvestmentTerm.objects.get(id=2)
    try:
        queryset=Company.objects.filter(investment_term=InvestmentTerm.objects.get(id=3))
    except ObjectDoesNotExist:
        queryset=Company.objects.none()    
