from .views import *
from django.urls import path

urlpatterns = [
  
  path('customers/<str:username>/', UserProfileView.as_view(), name='customer'),
  path('customers/update/<str:username>/',UpdateUserProfileView.as_view(), name='update_profile'),
  path('customers/', UserListView.as_view(), name='list_users'),

]