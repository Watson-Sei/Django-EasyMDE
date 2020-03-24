from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from markdown import markdown
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='edit_user')
    title = models.CharField(max_length=300)
    text = models.TextField()

    def get_text_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode='escape'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Edit'
        verbose_name_plural = 'Edit'
