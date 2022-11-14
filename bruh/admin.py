from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bruh.forms import CustomUserCreationForm, CustomUserChangeForm
from bruh.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name')
    list_filter = ('email',)
    fieldsets = (
        (None,
         {'fields': ('email', 'first_name', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
