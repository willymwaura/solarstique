from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics

#retrieves a list of all products or creates a new product.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
#retrieves, updates or deletes a specific product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# is responsible for listing all the purchases and creating a new purchase
class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

#is responsible for retrieving, updating, and deleting a single purchase
class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update product quantity if purchase quantity changed
        if 'quantity' in request.data:
            quantity_diff = request.data['quantity'] - instance.quantity
            instance.product.quantity -= quantity_diff
            instance.product.save()

        return Response(serializer.data)

















# from django.db.models import Sum, Count

# user = FndUser.objects.get(username='example_user')
# total_quantity = Purchase.objects.filter(user=user).aggregate(Sum('quantity'))['quantity__sum']
# total_cost = Purchase.objects.filter(user=user).aggregate(Sum('cost'))['cost__sum']
# num_purchases = Purchase.objects.filter(user=user).count()
# num_remaining_products = Product.objects.aggregate(Sum('quantity'))['quantity__sum']
