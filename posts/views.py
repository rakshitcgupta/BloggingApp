from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)
   # return HttpResponse("<h1>detail</h1>")

def post_list(request):
    #return HttpResponse("<h1>list</h1>")
    queryset=Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    # if request.user.is_authenticated():
    # 	context = {
    # 		"title": "My User List"
    # 	}
    # else:
    # 	context = {
    # 		"title": "List"
    # 	}
    return render(request,"index.html",context)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")
