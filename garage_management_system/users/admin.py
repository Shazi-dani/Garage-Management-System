from django.contrib import admin
from .models import BlacklistedToken, CustomUser


@admin.register(BlacklistedToken)
class BlacklistedTokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'blacklisted_at']
    readonly_fields = ['blacklisted_at']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'contact_no', 'user_type']
