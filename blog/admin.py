from django.contrib import admin
from blog.models import (Baloon, BaloonColor, BaloonSize, BaloonType, PriceBaloonSpecifications)
from django.utils.safestring import mark_safe
# Register your models here.



@admin.register(PriceBaloonSpecifications)
class PriceBaloonSpecificationsAdmin(admin.ModelAdmin):
    list_display = ['helium', 'painted', 'metallic', 'foil', 'created_at']
    search_fields = ['helium', 'painted', 'metallic', 'foil', 'created_at']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

@admin.register(BaloonColor)
class BallonColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields=['name']
    readonly_field = ['created_at']

@admin.register(BaloonSize)
class BaloonSizeAdmin(admin.ModelAdmin):
    list_display = ['inch', 'sm', 'created_at']
    search_fields = ['inch', 'sm']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

@admin.register(BaloonType)
class BaloonTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_price','description', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    readonly_fields = ['created_at']


@admin.register(Baloon)
class BaloonAdmin(admin.ModelAdmin):
    list_display = [
        'get_image', 'title', 'baloon_color', 'baloon_size', 
        'baloon_type', 'get_info', 'price', 'get_all_price', 'created_at'
    ]
    list_filter = [
        'baloon_color', 'baloon_size', 'baloon_type', 'is_helium', 
        'is_painted', 'is_metallic', 'is_foil', 'created_at'
    ]
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
    fieldsets = [
        (None, {
            'fields': ['image','title', 'description', 'price']
        }),
        ('Характеристики шарика', {
            'fields': ['price_specifications', 'baloon_color', 'baloon_size', 'baloon_type', 'is_helium', 'is_painted', 'is_metallic', 'is_foil']
        }),
        ('Дополнительная информация', {
            'fields': ['created_at'],
            'classes': ['collapse',]
        }),
    ]

    def get_image(self, obj):
        if obj.image:
            return mark_safe (f'<img src="{obj.image.url}" width="100"height="100">')
        else:
            "No Image"
    def get_all_price(self,obj):
        return obj.balloon_all_price()
    
    def get_info(self,obj):
        text = []
        if obj.is_helium:
            text.append("с гелием,")
        if obj.is_foil:
            text.append("фольгированный,")
        if obj.is_painted:
            text.append("с рисунком,")
        if obj.is_metallic:
            text.append("металлик")

        return "Шарик - "+" ".join(text)
    

    get_image.short_description = "Изображение"
    get_info.short_description = "Детали"
    get_all_price.short_description = "Общая цена"