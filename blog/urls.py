from django.urls import path

from . import views

urlpatterns=[
path('home',views.home,name="home"),
    path('profile',views.profile,name="profile"),
    path('addblogs',views.addblogs,name="addblogs"),
    path('<int:id>/',views.blogPage,name="blogPage"),
    path('<int:id>/edit',views.editBlog,name="editBlog"),
    path('<int:id>/delete',views.deleteBlog,name="deleteBlog")
    ] 