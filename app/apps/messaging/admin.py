from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    readonly_fields = ("name", "email", "message", "submitted_at")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(ContactMessage, ContactMessageAdmin)
