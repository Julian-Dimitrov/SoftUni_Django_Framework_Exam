from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import HwStoreUser, PhoneNumbersUserModel


class CustomUserAdmin(auth_admin.UserAdmin):
    fieldsets = auth_admin.UserAdmin.fieldsets + (("Not required personal info", {"fields": ["profile_bio", "age"]}),)
    add_fieldsets = auth_admin.UserAdmin.add_fieldsets + (("Not required personal info", {"fields": ["profile_bio", "age"]}),)

    list_display = ('pk', 'first_name', 'last_name', 'username', 'email', 'is_staff')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('pk', )


class CustomPhoneAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'user')


admin.site.register(HwStoreUser, CustomUserAdmin)
admin.site.register(PhoneNumbersUserModel, CustomPhoneAdmin)
