from django import forms

from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = [
            "title",
            "image",
            "content",
            "category"
        ]


class CategoryForm(forms.Form):
    CHOICES = (('Tech', 'Tech'),
               ('Food', 'Food'),
               ('Sports', 'Sports'),
               ('Fashion', 'Fashion'),)
    Select_Options = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)