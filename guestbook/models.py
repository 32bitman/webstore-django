from django.db import models


class Guestbook(models.Model):
    user = models.CharField(max_length=20, verbose_name="Карыстач")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Апублікавана")
    content = models.TextField(verbose_name="Змест")
    class Meta:
        ordering = ["-posted"]
        verbose_name = "запіс гасцёвай кнігі"
        verbose_name_plural = "запісы гасцёвай кнігі"
