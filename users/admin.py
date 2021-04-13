from django.contrib import admin
from . import models


# Register your models here.
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
