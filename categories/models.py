from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name="Назва")
    order = models.PositiveSmallIntegerField(default=0, unique=True, db_index=True, verbose_name="Парадкавы нумар")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "карэгорыя"
        verbose_name_plural = "катэгорыі"