from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'modified')
    list_filter = ('user', 'created', 'modified')
    search_fields = ('title', 'user__username') 
    list_per_page = 20
