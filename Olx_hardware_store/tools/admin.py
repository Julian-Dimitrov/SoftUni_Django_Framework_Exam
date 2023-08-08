from django.contrib import admin
from .models import Tool


class CustomToolAdmin(admin.ModelAdmin):
    fields = ('name', 'tool_photo', 'description', 'tool_country', 'tool_city', 'tool_price', 'user')
    list_display = ('pk', 'name', 'tool_price', 'user')
    search_fields = ('name', )
    ordering = ('pk', )
    list_filter = ('user', )


admin.site.register(Tool, CustomToolAdmin)
