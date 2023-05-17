from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import *
from .serializers import CarbonCreditSerializer, CarbonCreditPurchaseSerializer


class CarbonCreditListCreateView(generics.ListCreateAPIView):
    queryset = CarbonCredit.objects.all()
    serializer_class = CarbonCreditSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class CarbonCreditDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarbonCredit.objects.all()
    serializer_class = CarbonCreditSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarbonCreditPurchaseCreateView(generics.CreateAPIView):
    serializer_class = CarbonCreditPurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        credit_id = request.data.get('credit_id')
        credit = CarbonCredit.objects.get(id=credit_id)

        if credit.is_sold:
            return Response({'error': 'This credit has already been sold.'}, status=400)

        credit_price = credit.price_per_credit
        credit_amount = credit.credit_sold
        buyer = request.user
        purchase_total = credit_price * credit_amount

        if buyer.balance < purchase_total:
            return Response({'error': 'Insufficient balance to make purchase.'}, status=400)

        buyer.balance -= purchase_total
        credit.is_sold = True
        credit.sold_to = buyer
        buyer.save()
        credit.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(buyer=buyer, credit=credit)

        return Response(serializer.data)
    

class CarbonCreditPurchaseListView(generics.ListAPIView):
    serializer_class = CarbonCreditPurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CarbonCreditPurchase.objects.filter(buyer=self.request.user)

