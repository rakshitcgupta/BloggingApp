from urllib.parse import quote_plus
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import Post,Comment
from .models import UsersCategories
from .forms import PostForm
from .forms import CategoryForm
from .forms import CommentForm
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.views.generic import RedirectView
# Create your views here.
# def get_my_choices(request):
#     # you place some logic here
#     if request.user.is_authenticated:
#         username = request.user.username
#         obj = UsersCategories.objects.filter(user=username)
#         queryset1 = Post.objects.none()
#         choices_list=[]
#         for i in obj:
#             choices_list.append(i.category)
#     return choices_list
def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Created")
        # return HttpResponseRedirect('/posts/detail/')
        # return HttpResponseRedirect(instance.get_absolute_url())
        return HttpResponseRedirect("/")
    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    # comments = get_object_or_404(Comment,id=id)
    print(id)
    share_string=quote_plus(instance.content)
    if request.user.is_authenticated:
        obj = Comment.objects.filter(post=instance)

        context = {
            "title": instance.title,
            "instance": instance,
            "share_string":share_string,
            "comments":obj
        }
        # if request.user.is_authenticated:
    #     return redirect()
        return render(request, "post_detail.html", context)
   # return HttpResponse("<h1>detail</h1>")

def add_comment_to_post(request, id=None):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user=request.user
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form , 'button': "Save",})


def post_like(request,id=None):
    instance = get_object_or_404(Post, id=id)
    url_=instance.get_absolute_url()
    print(request.user)
    user = request.user
    if user.is_authenticated:
        if user in instance.likes.all():
            instance.likes.remove(user)
        else:
            instance.likes.add(user)

    return HttpResponseRedirect(url_)


#
# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         print(id)
#         obj=get_object_or_404(Post,id=id)
#         return obj.get_absolute_url()

def post_list(request):
    #return HttpResponse("<h1>list</h1>")
    # if not request.user.is_authenticated:
    #     queryset=Post.objects.all()
    #     context = {
    #         "object_list": queryset,
    #         "title": "List"
    #     }
    # else:
    if request.user.is_authenticated:
        username = request.user.username
        obj = UsersCategories.objects.filter(user=username)
        queryset1 = Post.objects.none()
        for i in obj:
            queryset2 = Post.objects.filter(category=i.category)
            queryset1 = (queryset1 | queryset2)
        query = request.GET.get("q")
        if query:
            queryset1=queryset1.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
                #auther ka baki hai
            ).distinct()
        context = {
            "object_list": queryset1,
            "title": "List"
        }
        return render(request, "post_list.html", context)
    else:
        return redirect("login/")
    # if request.user.is_authenticated():
    # 	context = {
    # 		"title": "My User List"
    # 	}
    # else:
    # 	context = {
    # 		"title": "List"
    # 	}

# def post_list(request):
#     #return HttpResponse("<h1>list</h1>")
#     queryset=Post.objects.all()
#     context = {
#         "object_list": queryset,
#         "title": "List"
#     }
#     # if request.user.is_authenticated():
#     # 	context = {
#     # 		"title": "My User List"
#     # 	}
#     # else:
#     # 	context = {
#     # 		"title": "List"
#     # 	}
#     return render(request,"post_list.html",context)

def post_latest(request):
    #return HttpResponse("<h1>list</h1>")
    # if not request.user.is_authenticated:
    #     queryset=Post.objects.all()
    #     context = {
    #         "object_list": queryset,
    #         "title": "List"
    #     }
    # else:
    if request.user.is_authenticated:
        username = request.user.username
        obj = UsersCategories.objects.filter(user=username)
        queryset1 = Post.objects.none()
        for i in obj:
            queryset2 = Post.objects.filter(category=i.category)
            queryset1 = (queryset1 | queryset2)
        query = request.GET.get("q")
        if query:
            queryset1=queryset1.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
                #auther ka baki hai
            ).distinct()
        context = {
            "object_list": queryset1.order_by('-timestamp'),
            "title": "List"
        }
        return render(request, "post_list.html", context)
    else:
        return redirect("login/")


def post_popular(request):
    #return HttpResponse("<h1>list</h1>")
    # if not request.user.is_authenticated:
    #     queryset=Post.objects.all()
    #     context = {
    #         "object_list": queryset,
    #         "title": "List"
    #     }
    # else:
    if request.user.is_authenticated:
        username = request.user.username
        obj = UsersCategories.objects.filter(user=username)
        queryset1 = Post.objects.none()
        for i in obj:
            queryset2 = Post.objects.filter(category=i.category)
            queryset1 = (queryset1 | queryset2)
        query = request.GET.get("q")
        if query:
            queryset1=queryset1.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
                #auther ka baki hai
            ).distinct()
        context = {
            "object_list": queryset1.annotate(like_count=Count('likes')).order_by('-like_count'),
            "title": "List"
        }
        return render(request, "post_list.html", context)
    else:
        return redirect("login/")





def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:post_details")


def select_category(request):
    title = "Genre"
    button = "Save"
    # if request.method == 'POST':
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        Select_Options = form.cleaned_data.get('Select_Options')
        # print(Select_Options)
        if request.user.is_authenticated:
            username = request.user.username
            UsersCategories.objects.filter(user=username).delete()
            for i in Select_Options:
                # list = UsersCategories.objects.filter(user=username, category=i)
                # if (list.count() == 0):
                category = UsersCategories(user=username, category=i)
                category.save()
            # return post_list(request)
            return redirect("/")
    # else:
    #     obj = UsersCategories.objects.filter(user=request.user.username)
    #     cat=obj.category
    #     form = CategoryForm(cat)
    return render(request, "category.html", {'form': form, 'title': title, 'button':button})
