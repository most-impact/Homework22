from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'number_views', 'publication')
    search_fields = ('title',)
    list_filter = ('publication', 'created_at')
    ordering = ('-created_at',)