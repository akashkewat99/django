from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Post
from django.shortcuts import render
from . forms import PostForm
from django.http import HttpResponse,JsonResponse

def main(request):
    return render(request,'blog/main.html',{'context':None})

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/postcreate.html'
    # fields = ['title','content']
    form_class = PostForm
    success_url = '/blogs/list/'



class PostUpdate(UpdateView):
    model = Post
    template_name = 'blog/postcreate.html'
    fields = ['title','content']
    success_url = '/blogs/list/'


class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/postDelete.html'
    success_url = '/blogs/list/'