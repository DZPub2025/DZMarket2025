from django.contrib import admin
from .models import Category, Ad, AdImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title','seller','price','wilaya','is_published','created_at')
    list_filter = ('is_published','wilaya','category')

@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    pass
