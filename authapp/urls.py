from .views import *
from django.urls import path

urlpatterns = [
    path('register', RegistrationAPIView.as_view(), name='AuthRegistry'),
    path('login', LoginApiView.as_view(), name='login'), 
    path('user', FndUserRetrieveupdateApiView.as_view(),name='updateUser')

]