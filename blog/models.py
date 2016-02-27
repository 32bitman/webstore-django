from django.contrib.auth.models import User
from django.db import models
from django_comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Загаловак")
    description = models.TextField(verbose_name="Скарочаны змест")
    content = models.TextField(verbose_name="Змест")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Апублікавана")
    is_commentable = models.BooleanField(default=True, verbose_name="Дазвол каментавання")
    tags = TaggableManager(blank=True, verbose_name="Тэгі")
    user = models.ForeignKey(User, editable=False)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-posted"]
        verbose_name = "артыкул блогу"
        verbose_name_plural = "артыкулы блогу"

class BlogModerator(CommentModerator):
    email_notification = True
    enable_field = "is_commentable"
moderator.register(Blog, BlogModerator)
