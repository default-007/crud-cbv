from django import forms
from .models import *

class PostsForm(forms.ModelForm):
  class Meta:
    model = Core
    fields = "__all__"