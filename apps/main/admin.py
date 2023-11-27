from django.contrib import admin
from .models import Film, Serial
# Register your models here.

@admin.register(Film)
class FilmsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'year',
        'image',
    )
    list_display_links = (
        'title',
    )

    search_fields = (

        'title',
        'desc',
        'year',
        'image',
    )


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'year',
        'image',
        'count_series',
    )
    list_display_links = (
        'title',
    )

    search_fields = (

        'title',
        'desc',
        'year',
        'image',
        'count_series',
    )