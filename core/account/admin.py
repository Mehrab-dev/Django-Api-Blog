from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from account.models import User , Profile

class CustomUserAdmin(UserAdmin) :
    model = User
    list_display = ["id","email","is_superuser","is_staff","is_active","is_verified"]
    list_display_links = ["id","email"]
    list_filter = ["is_superuser","is_staff","is_active","is_verified"]
    search_fields = ["id","email"]
    ordering = ("id",)

    fieldsets = (
        ("Authentication",{
            "fields":("email","password"),
        }),
        ("Permissions",{
            "fields":("is_superuser","is_staff","is_active","is_verified"),
        }),
        ("Group Permissions",{
            "fields":("groups","user_permissions"),
        }),
        ("Important Date",{
            "fields":("last_login",),
        }),
    )

    add_fieldsets = (
        (None,{
            "classes":("wide",),
            "fields":("email","password1","password2","is_superuser","is_staff","is_active","is_verified"),
        }),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)