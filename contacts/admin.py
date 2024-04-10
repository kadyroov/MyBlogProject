from django.contrib import admin
from contacts.models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'is_painted', 'is_helium', 'is_metallic','is_foil']
    search_fields = ['name', 'phone']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

