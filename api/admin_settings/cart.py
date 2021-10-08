from django.contrib import admin



class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cartId', )
    list_display_links = ('id', 'cartId')
    search_fields = ('id', 'cartId')
    fields = ('cartId',)