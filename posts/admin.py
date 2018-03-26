from django.contrib import admin

# Register your models here.
from .models import Post
from .models import UsersCategories
from .models import Comment
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp","category"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title","category"]
    search_fields = ["title","content","category"]
    class Meta:
        model = Post
admin.site.register(Post,PostModelAdmin)
admin.site.register(UsersCategories)
admin.site.register(Comment)