from django.contrib import admin
from .models import Betslip

# Register your models here.

@admin.register(Betslip)
class BetslipAdmin(admin.ModelAdmin):
    list_display = ('slip_code', 'bookmaker', 'status', 'checked_at')
    search_fields = ('slip_code', 'bookmaker')
    list_filter = ('status',)
    ordering = ('-checked_at',)

    def has_add_permission(self, request, obj=None):
        return False  # Disable adding new slips through the admin interface