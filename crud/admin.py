from django.contrib import admin
from .models import USER
# Register your models here.

@admin.register(USER)
class UserAdmin(admin.ModelAdmin):
    list_display=("id","name","email","password")