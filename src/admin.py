from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin  # Import MPTTModelAdmin from mptt.admin

admin.site.register(blog)
admin.site.register(blog_category)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'phone', 'email')
    list_per_page = 20


admin.site.register(user_profile, UserProfileAdmin)

# admin.py

from django.contrib import admin
from mptt.admin import MPTTModelAdmin  # Import MPTTModelAdmin from mptt.admin
from .models import Comment


class CommentAdmin(MPTTModelAdmin):  # Use MPTTModelAdmin as the base admin class
    list_display = ('user', 'blog_id', 'content', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('user__name', 'blog_id__title', 'content')
    list_per_page = 20


admin.site.register(Comment, CommentAdmin)  # Register Comment model with CommentAdmin
