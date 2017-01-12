from django.db import models
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
        

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    author = models.CharField(max_length=30, default = "Matt McGovern")
    tag = TaggableManager()
    
    
    objects = EntryQuerySet.as_manager()
    
    def __str__(self):
        return self.title
    
    def get_year(self):
        return self.date.year   
    
    def approved_comments(self):
        return self.comments.filter(comment_approved=True)    
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-date"]
        
        
class Extra(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Extra Page"
        verbose_name_plural = "Extra Pages"
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length = 200)
    body = models.TextField()
    comment_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    website = models.URLField(blank=True)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.body
