from django.contrib import admin
from .models import Signup  # ✅ Import the model from models.py

class Swsignup(admin.ModelAdmin):
    list_display = ['NAME', 'EMAIL', 'PAS']

admin.site.register(Signup, Swsignup)