from django.views.generic import (TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Post


class HomePageView(ListView):
    template_name='blog/index.html'
    model=Post


class AboutPageView(TemplateView):
    template_name='blog/about.html'


class PostCreateView(CreateView):
    template_name='blog/post-create.html'
    model=Post
    fields=['title','content']


class PostDetailView(DetailView):
    template_name='blog/post-detail.html'
    model=Post
    context_object_name='post'


class PostUpdateView(UpdateView):
    template_name='blog/post-update.html'
    model=Post
    fields=['title','content']
    

class PostDeleteView(DeleteView):
    template_name='blog/post-delete.html'
    context_object_name='post'
    success_url='/'
    model=Post


