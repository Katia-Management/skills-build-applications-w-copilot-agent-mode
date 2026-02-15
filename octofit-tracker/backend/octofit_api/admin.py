from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'activity_type', 'duration_minutes', 'created_at')
    search_fields = ('user_name', 'activity_type')
