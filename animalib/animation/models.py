from time import timezone
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='animation_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    favorites = models.ManyToManyField(
        User, related_name='favorite', default=None, blank=True)
    objects = models.Manager()
    newmanager = NewManager()

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title
