from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bruh.forms import CustomUserCreationForm, CustomUserChangeForm
from bruh.models import CustomUser, Visitor, Contact


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


class VisitorAdmin(admin.ModelAdmin):
    model = Visitor
    list_display = ('id', 'ipaddress', 'city', 'state', 'country', 'latitude', 'longitude', 'zipcode', 'when_visited')
    search_fields = ('id', 'ipaddress', 'city', 'state', 'country', 'latitude', 'longitude', 'zipcode', 'when_visited')
    list_filter = ('id', 'ipaddress', 'city', 'state', 'country', 'latitude', 'longitude', 'zipcode', 'when_visited')


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('id', 'name', 'email', 'message', 'when_sent')
    search_fields = ('id', 'name', 'email', 'message', 'when_sent')
    list_filter = ('id', 'name', 'email', 'message', 'when_sent')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Contact, ContactAdmin)
