from django.contrib import admin
from .models import Post 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'source')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'publish', 'author')
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'

