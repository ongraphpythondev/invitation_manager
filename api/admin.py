# Django Package Import
from django.contrib import admin
# Project Import
from .models import Invitation

# Register your models here.
admin.site.register(Invitation)
