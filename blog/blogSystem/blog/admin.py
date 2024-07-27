from django.contrib import admin
# Register your models here.
from .models import Post

# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ['title','content','created_at']
    list_filter = ['title']
    list_editable = ['content']


admin.site.register(Post,PostAdmin)