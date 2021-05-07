from django.contrib import admin
from .models import Item, OrderItem, Order


def make_visible(modeladmin, request, queryset):
    queryset.update(is_visible=True)


def make_no_visible(modeladmin, request, queryset):
    queryset.update(is_visible=False)


def make_quantity_one(modeladmin, request, queryset):
    queryset.update(quantity=1)


def make_quantity_zero(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible', 'quantity', 'time_added']
    ordering = ['time_added']
    actions = [make_visible, make_no_visible, make_quantity_one, make_quantity_zero]


make_visible.short_description = "Zmień status zaznaczonych elementów na widoczny"
make_no_visible.short_description = "Zmień status zaznaczonych elementów na niewidoczny"

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
