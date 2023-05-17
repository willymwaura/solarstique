from django.urls import path
from .views import *
    

app_name = 'carbon_credits'

urlpatterns = [
    path('credits/', CarbonCreditListCreateView.as_view(), name='credit_list_create'),
    path('credits/<int:pk>/', CarbonCreditDetailView.as_view(), name='credit_detail'),
    path('credits/purchase/', CarbonCreditPurchaseCreateView.as_view(), name='credit_purchase'),
    path('credits/purchased/', CarbonCreditPurchaseListView.as_view(), name='credit_purchase_list'),
]
