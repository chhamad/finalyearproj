# mainapp/models.py

from django.db import models
from .user import CustomUser  # Import the CustomUser model

# Review model with attributes and ForeignKey relationships with CustomUser (Client and Lawyer)
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_reviews')
    lawyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='lawyer_reviews')
    review_score = models.IntegerField()
    review_detail = models.TextField()
