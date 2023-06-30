from django.contrib import admin
from .models import Post, Author, Tag , Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date")
    list_display = ("title", "date", "author")   #list_display is django pre=assigned
    prepopulated_fields = {"slug":("title",)} #pre-populates the slug. , is requied to make it a tuple


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)