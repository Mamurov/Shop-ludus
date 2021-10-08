from django.contrib import admin
from django.utils.safestring import mark_safe



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'get_html_photo', 'email')
    list_display_links = ('id', 'email', 'name')
    search_fields = ('name', 'email')
    fields = ('name', 'surname', 'avatar', 'email', 'password', 'shop')

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"