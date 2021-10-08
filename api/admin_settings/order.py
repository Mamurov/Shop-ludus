from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', )
    list_display_links = ('id',)
    search_fields = ('id',)
