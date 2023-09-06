# mainapp/models.py

from django.db import models
from .case import Case


# Contract model with attributes and ForeignKey relationship with Case
class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    date = models.DateField()
    detail = models.TextField()
