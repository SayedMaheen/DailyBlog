from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from bloguser.models import User 


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1','password2','email','first_name','last_name' )
        }),

    )

