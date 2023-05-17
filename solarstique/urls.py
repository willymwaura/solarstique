
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls')),
    path('', include('customers.urls')),
    # path('', include('carbon.urls')),
    path('', include('products.urls')),
]
