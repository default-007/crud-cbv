from django.contrib import admin
from .models import Core

@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
  prepopulted_fields = {'slug': ('title'),}
# Register your models here.
