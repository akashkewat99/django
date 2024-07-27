from django.contrib import admin
from django.urls import path
from .views import PostList,PostCreate,main,PostUpdate,PostDelete

urlpatterns = [
    path('',main,name="Home"),
    path('blogs/list/',PostList.as_view(),name="PostList"),
    path('blogs/create/',PostCreate.as_view(),name="PostCreate"),
    path('blogs/update/<int:pk>/',PostUpdate.as_view(),name="PostUpdate"),
    path('blogs/delete/<int:pk>/',PostDelete.as_view(),name="PostDelete"),

]