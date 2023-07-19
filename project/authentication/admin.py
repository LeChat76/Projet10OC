from django.contrib import admin
from authentication.models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'birthday',
        'can_be_contacted',
        'can_data_be_shared',
    )
    exclude = ['password', 'user_permissions', 'groups', 'groupstatut']

admin.site.register(Users, UserAdmin)
