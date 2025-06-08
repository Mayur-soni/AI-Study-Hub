from django.contrib import admin

from aiapp.models import Signup


# Register your models here.
class Swsignup(admin.ModelAdmin):
    list_display = ['NAME','EMAIL','PAS']
    list_per_page = 3
    search_fields = ['NAME','EMAIL']

admin.site.register(Signup,Swsignup)