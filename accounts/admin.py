from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from .models import User as MyUser,shipping_address,customer_profile
from .forms import user_register_form,UserAdminChangeForm

# Register your models here.


admin.site.register(customer_profile)
admin.site.register(shipping_address)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm     #edit form upddate hash view hashing the password django documentation 
    add_form = user_register_form       # actual form create view

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










#admin.site.unregister(User)

admin.site.register(MyUser)

#User= get_user_model()
# class UserAdmin(admin.ModelAdmin):
#     search_fields= ['email']
#     class Meta:
#         model = User

# admin.site.register(User,UserAdmin)