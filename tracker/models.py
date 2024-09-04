from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Record(models.Model):
    user_id = models.IntegerField(default=0)
    date = models.DateField(auto_now=False)
    all_categories = [
        ("Utility", "Utility"),
        ("Food", "Food"),
        ("Gas", "Gas"),
        ("Mortgage/Rent", "Mortgage/Rent"),
        ("Transportation", "Transportation"),
        ("Subscriptions", "Subscriptions"),
        ("Healthcare", "Healthcare"),
        ("Personal Expenses", "Personal Expenses"),
        ("Other", "Other")
    ]
    category = models.CharField(default="Other", max_length=255, choices=all_categories)
    location = models.CharField(max_length=100, default="")
    memo = models.TextField(max_length=200, default="")
    expense = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    
    def serialize(self):
        return {
            "date": self.date,
            "category": self.category,
            "location": self.location,
            "memo": self.memo,
            "expense": self.expense,
            "id": self.id
        }