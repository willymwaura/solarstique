# from django.db import models
# from django.contrib.auth.models import User
# from .models import FndUser



# class CarbonCredit(models.Model):
#     seller = models.ForeignKey(FndUser, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)
#     credit_sold = models.DecimalField(max_digits=10, decimal_places=2)
#     price_per_credit = models.DecimalField(max_digits=10, decimal_places=2)
#     is_sold = models.BooleanField(default=False)
#     sold_to = models.ForeignKey(FndUser, related_name='sold_credits', on_delete=models.CASCADE, null=True, blank=True)


#     def __str__(self):
#         return f"{self.credit_sold} credits from {self.seller} sold to {self.sold_to}"
    

# class CarbonCreditPurchase(models.Model):
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     credit_purchased = models.ForeignKey(CarbonCredit, on_delete=models.CASCADE)
#     purchased_at = models.DateTimeField(auto_now_add=True)
#     is_complete = models.BooleanField(default=False)

    
#     def __str__(self):
#         return f"{self.credit_purchased} credits purchased by {self.buyer.username} at {self.purchased_at}"
