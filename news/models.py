from django.db import models
from django.utils.timezone import now


class New(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Загаловак")
    description = models.TextField(verbose_name="Скарочаны змест")
    content = models.TextField(verbose_name="Поўны змест")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Апублікавана")

    class Meta:
        ordering = ["-posted"]
        verbose_name = "навіна"
        verbose_name_plural = "навіны"
