from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # armazenado como HTML (renderizar com |safe)
    posted_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f'{self.author} em {self.post}'