from django.contrib import admin
from django.contrib.auth.models import Group, User

class UserInline(admin.TabularInline):
    model = Group.user_set.through
    extra = 1  # Number of empty forms to display

class GroupAdmin(admin.ModelAdmin):
    inlines = [UserInline]

# Unregister the default Group admin
admin.site.unregister(Group)
# Register the customized Group admin
admin.site.register(Group, GroupAdmin)
