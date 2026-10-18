from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.catalog.models import Category


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    mptt_level_indent = 40
    prepopulated_fields = {'slug':('name',)}
