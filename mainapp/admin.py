# mainapp/admin.py

from django.contrib import admin
from .models import CustomUser, Case, Review, ChatMessage, Contract

# Register your models here
admin.site.register(CustomUser)

admin.site.register(Case)
admin.site.register(Review)
admin.site.register(ChatMessage)
admin.site.register(Contract)
