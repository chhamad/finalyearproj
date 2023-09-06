from django.db import models
from .user import CustomUser  # Import the CustomUser model

class Hiring(models.Model):
    hiring_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_hirings')
    hired_lawyers = models.ManyToManyField(CustomUser, related_name='hired_lawyers')
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Hiring ID: {self.hiring_id} - Client: {self.client.user.username}"

    class Meta:
        ordering = ['-hire_date']