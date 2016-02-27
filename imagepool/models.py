from django.contrib.auth.models import User
from django.db import models


class ImagePool(models.Model):
    user = models.ForeignKey(User)
    uploaded = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name="Выгружаны")
    image = models.ImageField(upload_to="imagepool/%Y/%m", verbose_name="Выява")

    class Meta:
        ordering = ["user", "-uploaded"]
        verbose_name = "выява"
        verbose_name_plural = "выявы"

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(ImagePool, self).delete(*args, **kwargs)
