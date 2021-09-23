from django.contrib import admin
from django.contrib.auth.models import Group
from drf_core.admin import BaseModelAdmin

from rest_framework.authtoken.models import Token

from accounts.models import User


admin.site.unregister(Token)
admin.site.unregister(Group)


# =============================================================================
# User
# =============================================================================
@admin.register(User)
class UserAdmin(BaseModelAdmin):
    """
    Customize User Admin
    """
    list_display = [
        'id',
        'email',
        'first_name',
        'last_name',
        'auth_provider',
    ]
