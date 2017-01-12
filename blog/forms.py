#forms

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'body', 'website', 'email',)
        labels = {
            'author': "Name *", 'body': "Comment", 'email': 'Email *'
            }