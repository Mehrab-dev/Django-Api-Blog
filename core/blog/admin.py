from django.contrib import admin

from blog.models import Post , Category

class PostAdmin(admin.ModelAdmin) :
    model = Post
    list_display = ["id","title","author","status","published_date"] 
    list_display_links = ["id","title"]
    list_filter = ["status"]
    search_fields = ["author"]
    ordering = ("id",)
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
