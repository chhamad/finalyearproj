from django.db import models
from .user import CustomUser  # Import the CustomUser model

class Case(models.Model):
    STATUS_CHOICES = (
        ('waiting_for_approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    case_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_cases')
    lawyer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='lawyer_cases',
        null=True,  # Make the field nullable
        blank=True,  # Allow an empty value
    )
    case_detail = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting_for_approval')

    def __str__(self):
        return f"Case ID: {self.case_id} - Status: {self.get_status_display()}"

    class Meta:
        ordering = ['-case_id']