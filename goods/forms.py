from goods.models import Good
from django.forms import ModelForm


class GoodForm(ModelForm):

    class Meta:
        model = Good
        fields = ["name", "category", "description", "content", "price", "price_acc", "in_stock", "featured", "image"]
