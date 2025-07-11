from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    fields = ("name", "url", "order")
    extra = 1
    ordering = ("order",)


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
