from django import forms
# from .views import get_my_choices
from .models import Post
from .models import Comment
from .models import UsersCategories

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
    # initial = ('Tech','Food')

    # def __init__(self, user, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     initial='Tech'
    #

        # self.Select_Options.queryset = UsersCategories.objects.filter(user=user)
    # my_choices=[]
    #     if request.user.is_authenticated:
    #     #         username = request.user.username
    #     #         obj = UsersCategories.objects.filter(user=username)
    #     #         queryset1 = Post.objects.none()
    #     #         choices_list=[]
    #     #         for i in obj:
    #     #             choices_list.append(i.category)
    #     #     return choices_list
    # MY_CHOICES = get_my_choices()
    # initial=(c[0] for c in MY_CHOICES)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)