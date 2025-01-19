from django import forms
from django.db import models

class Queue(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=15)
    address_choices = [
        ('Address1', 'Manzil 1'),
        ('Address2', 'Manzil 2'),
    ]
    address = models.CharField(max_length=20, choices=address_choices)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
