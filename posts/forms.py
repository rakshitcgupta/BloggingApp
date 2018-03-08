from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = [
            "title",
            "content",
            "category"
        ]


class CategoryForm(forms.Form):
    CHOICES = (('Tech', 'Tech'),
               ('Food', 'Food'),
               ('Sports', 'Sports'),
               ('Fasion', 'Fasion'),)
    Select_Options = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())