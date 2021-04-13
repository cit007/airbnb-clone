from django.contrib import admin
from . import models


# Register your models here.
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
# @admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User, CustomUserAdmin)
