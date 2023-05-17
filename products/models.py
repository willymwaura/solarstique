from django.db import models
from django.http import JsonResponse
from django.urls import reverse
# from .models import FndUser


# fetch('/get-products/')
#   .then(response => response.json())
#   .then(data => {
#     console.log(data);
#     // Do something with the product information
#   });



# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=200)  # Update the field to URLField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    

# product1 = Product(name='Ayogu', description='Named after the father of our founder and CEO.They are specially made for cooling drinks, dairy products, etc en route to markets, stalls, or homes.This prototype model is a 150 Litre capacity and can be scaled up to 1000 liters.', price=10, image='assets/images/ayo 2.jpeg')
# product1.save()
# product2 = Product(name='Solar Cold Room', description='Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', price=10, image='assets/images/freezer-2.jpg')
# product2.save()
# product3 = Product(name='Chill Tent', description='chill tents are a cubic meter cold storage box that uses “liquid ice” as its coolant. It is specially made for fruits and vegetable farmers and sellers. They are solar and salt water powered', price=10, image='assets/images/chill tent.jpeg')
# product3.save()
# product4 = Product(name='Ice Blocks ', description='special ice blocks that does not defrost for 4 days. The Ice block is made using special food preservation solution that also helps to keep the food item fresh and preserved.', price=30, image='assets/images/Ice Blocks.png')
# product4.save()
# product5 = Product(name='400ltrs Freezer', description='Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum..', price=10, image='assets/images/freezer-3.jpg')
# product5.save()
# product6 = Product(name='Tricycled freezers', description='It is a detachable tricycle Mobile solar freezer. They are specially made for cooling perishable products en route to markets, stalls, or homes.It is totally solar-powered and works with little or no battery backup.', price=10, image='assets/images/Tricycled freezers.png')
# product6.save()
# product7 = Product(name='Tricycled freezers', description='It is a detachable tricycle Mobile solar freezer. They are specially made for cooling perishable products en route to markets, stalls, or homes.It is totally solar-powered and works with little or no battery backup.', price=10, image='assets/images/Tricycled freezers.png')
# product7.save()
# product8 = Product(name='Tricycled freezers', description='It is a detachable tricycle Mobile solar freezer. They are specially made for cooling perishable products en route to markets, stalls, or homes.It is totally solar-powered and works with little or no battery backup.', price=10, image='assets/images/Tricycled freezers.png')
# product8.save()
# product9 = Product(name='Tricycled freezers', description='It is a detachable tricycle Mobile solar freezer. They are specially made for cooling perishable products en route to markets, stalls, or homes.It is totally solar-powered and works with little or no battery backup.', price=10, image ='assets/images/Tricycled freezers.png')
# product9.save()


def get_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)
    
class Purchase(models.Model):
    # user = models.ForeignKey(FndUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update product quantity and save purchase
        self.product.quantity -= self.quantity
        self.product.save()
        super(Purchase, self).save(*args, **kwargs)