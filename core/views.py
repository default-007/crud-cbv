from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView
# Create your views here.
class IndexView(ListView):
  model = Core
  template_name = 'index.html'
  context_object_name = 'index'

class SingleView(DetailView):
  model=Core
  template_name = 'single.html'
  context_object_name = 'post'

class PostsView(ListView):
  model=Core
  template_name = 'posts.html'
  context_object_name = 'post_list'

class AddView(CreateView):
  model=Core
  template_name = 'add.html'
  fields = '__add__'
  success_url = reverse_lazy('core:posts')