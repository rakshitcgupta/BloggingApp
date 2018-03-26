from django.contrib import admin
from django.urls import path,include

from posts import views
# from posts.views import PostLikeRedirect

urlpatterns = [
    path('', views.post_list,name='posts'),
    path('create/', views.post_create,name='post_create'),
    path('category/', views.select_category,name='select_category'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/like', views.post_like, name='post_like'),
    path('<int:id>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    # path('<int:id>/like/', PostLikeRedirect.as_view(), name='like'),
    path('update', views.post_update),
    path('delete', views.post_delete),
]



