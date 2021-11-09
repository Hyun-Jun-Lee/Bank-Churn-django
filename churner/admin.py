from django.contrib import admin
from .models import PredResults
# Register your models here.

@admin.register(PredResults)
class PredResultsAdmin(admin.ModelAdmin):
    pass