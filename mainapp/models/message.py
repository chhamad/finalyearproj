# mainapp/models.py

from django.db import models
from .user import CustomUser

# Message model with attributes and ManyToManyField relationship with CustomUser (Sender and Receiver)
class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body
