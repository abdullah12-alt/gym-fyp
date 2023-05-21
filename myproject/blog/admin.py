from django.contrib import admin
from .models import blog

class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on' ,'blog_image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(blog, blogAdmin)