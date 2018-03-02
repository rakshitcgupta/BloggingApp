from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        # return HttpResponseRedirect('/posts/detail/')
        return HttpResponseRedirect(instance.get_absolute_url())
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
    return render(request,"post_list.html",context)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:post_details")