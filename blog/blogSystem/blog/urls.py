from django.contrib import admin
from django.urls import path,include
from .views import PostList,PostCreate

urlpatterns = [
    path('blogs/list/',PostList.as_view(),name="PostList"),
    path('blogs/create/',PostCreate.as_view(),name="PostCreate"),

]