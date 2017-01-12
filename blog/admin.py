from django.contrib import admin
from django.db import models
from blog.models import Post, Extra, Comment
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug":("title",)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }    

class ExtraAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug":("title",)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }  
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "date", "author", "comment_approved")
    

admin.site.register(Post, EntryAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Comment, CommentAdmin)