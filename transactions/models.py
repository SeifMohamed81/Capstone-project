from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.amount}by {self.user.username}"
