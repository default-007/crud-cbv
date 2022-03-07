from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Core(models.Model):
  title = models.CharField(max_length=200)
  excerpt = models.TextField(max_length=500)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core', null=True)
  slug = models.SlugField(max_length=100)
  published = models.DateTimeField(default=timezone.now)

  def get_absolute_url(self):
    return reverse('core:single', args=[self.slug])

  class Meta:
    #odering = ['-published']
    pass

  def __str__(self):
    return self.title