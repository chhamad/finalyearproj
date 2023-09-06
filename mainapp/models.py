# mainapp/models.py

from django.db import models
from django.contrib.auth.models import User

# User model with additional fields for User_Type (Lawyer or Client)
class CustomUser(models.Model):
    USER_TYPES = (
        ('Lawyer', 'Lawyer'),
        ('Client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

# Lawyer model with attributes and a One-to-One relationship with CustomUser
class Lawyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    lawyer_id = models.AutoField(primary_key=True)
    bio = models.TextField()
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

# Client model with attributes and a One-to-One relationship with CustomUser
class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    client_id = models.AutoField(primary_key=True)

# Case model with attributes and ForeignKey relationships with Client and Lawyer
class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    case_detail = models.TextField()

# Review model with attributes and ForeignKey relationships with Client and Lawyer
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    review_score = models.IntegerField()
    review_detail = models.TextField()

# Message model with attributes and ManyToManyField relationship with CustomUser (Sender and Receiver)
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender_user = models.ManyToManyField(CustomUser, related_name='sent_messages')
    receiver_user = models.ManyToManyField(CustomUser, related_name='received_messages')
    message_detail = models.TextField()

# Contract model with attributes and ForeignKey relationship with Case
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    date = models.DateField()
    detail = models.TextField()
