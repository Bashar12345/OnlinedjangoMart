from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth import get_user_model
from .models import User,shipping_address,customer_profile
from .forms import user_register_form,UserAdminChangeForm,UserAdminCreationForm

# Register your models here.
User= get_user_model()

admin.site.register(customer_profile)
admin.site.register(shipping_address)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm             #edit form
    add_form = UserAdminCreationForm       # actual form

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()












admin.site.register(User)

# class UserAdmin(admin.ModelAdmin):
#     search_fields= ['email']
#     class Meta:
#         model = User

# admin.site.register(User,UserAdmin)