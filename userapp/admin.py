from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# class CustomUserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('mobile_number', 'password')}),
#         ('Personal info', {'fields': ('name', 'email', 'date_of_birth', 'gender', 'pan_card', 'profile_image')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_mobile_verified')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('mobile_number', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('mobile_number', 'name', 'email', 'is_staff', 'is_superuser')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_mobile_verified')
#     search_fields = ('mobile_number', 'name', 'email')
#     ordering = ('mobile_number',)

# admin.site.register(User, CustomUserAdmin)
admin.site.register(User)
