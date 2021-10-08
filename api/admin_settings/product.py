from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id',)
    search_fields = ('id',)
