from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserInline(admin.TabularInline):
    model = Group.user_set.through
    extra = 1  # Number of empty forms to display

class GroupAdmin(admin.ModelAdmin):
    inlines = [UserInline]

# Customizing User Admin to manage group permissions
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]
    filter_horizontal = ('groups',)  # Improved UI for managing groups

# Unregister the default Group and User admin
admin.site.unregister(Group)
admin.site.unregister(User)

# Register the customized Group and User admin
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
