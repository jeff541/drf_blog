from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog
class CustomUserAdmin(UserAdmin):
    list_display =("username", "first_name", "last_name", 'is_staff', 'bio', 'profile_picture', 'facebook', 'instagram')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at','published_date','is_draft','category')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)