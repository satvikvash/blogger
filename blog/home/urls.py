from django.urls import path
from .views import Home,PostDetail,AddPost,UpdatePost, DeletePost, CategoryView, LikesView

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('blog/<int:pk>',PostDetail.as_view(),name="post"),
    path('addpost/',AddPost.as_view(),name="addpost"),
    path('blog/update/<int:pk>',UpdatePost.as_view(),name="updatepost"),
    path('blog/delete/<int:pk>',DeletePost.as_view(),name="deletepost"),
    path('category/<str:cats>',CategoryView,name="category"),
    path('likes/<int:pk>',LikesView,name="likes"),
]
