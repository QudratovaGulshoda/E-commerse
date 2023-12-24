from django.db import models
from utils.models import BaseModel
# Create your models here.
from django.utils.html import format_html


class Product(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='images/')
    price = models.IntegerField()

    status = models.CharField(max_length=8, choices=(
        ('active', 'active'),
        ('noactive', 'no active')
    ), default='noactive')

    def __str__(self):
        return self.name

    @property
    def picture(self):
        return format_html('<img src="{}" width="50" heigth="50" style="border-radius:50%"/>'.format(self.photo.url))

    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'Product '
        verbose_name_plural = 'Products '
