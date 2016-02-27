from django.core.urlresolvers import reverse
from django.db import models
from django_comments.moderation import moderator, CommentModerator
from categories.models import Category

class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Назва")
    category = models.ForeignKey(Category, verbose_name="Катэгорыя")
    description = models.TextField(verbose_name="Скарочанае апісанне")
    content = models.TextField(verbose_name="Поўнае апісанне")
    price = models.FloatField(db_index=True, verbose_name="Кошт, Br.")
    price_acc = models.FloatField(null=True, blank=True, verbose_name="Кошт са зніжкай, Br.")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="У наяўнасці")
    featured = models.BooleanField(default=False, db_index=True, verbose_name="Прапануемы")
    image = models.ImageField(upload_to="goods/list", verbose_name="Асноўная выява")

    def save(self, *args, **kwargs):
        try:
            this_record = Good.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(Good, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Good, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("goods_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "тавар"
        verbose_name_plural = "тавары"


class GoodImage(models.Model):
    good = models.ForeignKey(Good)
    image = models.ImageField(upload_to="goods/detail", verbose_name="Дадатковая выява")

    def save(self, *args, **kwargs):
        try:
            this_record = GoodImage.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(GoodImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(GoodImage, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "выява да тавару"
        verbose_name_plural = "выявы да тавару"


class GoodModerator(CommentModerator):
    email_notification = True
moderator.register(Good, GoodModerator)
