from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

# Create your views here.
def index(request):
  posts = Core.objects.all()
  context = {'posts':posts,}
  return render(request, 'index.html', context)
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
  fields = '__all__'
  success_url = reverse_lazy('core:posts')

class EditView(UpdateView):
  model=Core
  template_name = 'edit.html'
  fields = '__all__'
  pk_url_kwargs = 'pk'
  success_url = reverse_lazy('core:posts')

class DeleteView(DeleteView):
  model=Core
  pk_url_kwargs = 'pk'
  success_url = reverse_lazy('core:posts')
  template_name = 'confirm-delete.html'

#Django_rest_framework
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]