from django.contrib import admin
from .models import Remember

@admin.register(Remember)
class RemembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'user_id')
