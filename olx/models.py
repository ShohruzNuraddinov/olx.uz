from django.db import models
from django.db.models.functions import Coalesce

from user.models import UserModel as User
from utils.models import BaseModel
# Create your models here.


class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class District(BaseModel):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='districts')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_categories'
    )
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Brand(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BisnesStatus(models.Choices):
    phisical = 'Jismoniy'
    biznes = 'Biznes'


class AdsStatus(models.Choices):
    new = 'Yangi'
    fb = 'F/B'


class CurrencyChoise(models.Choices):
    uzs = 'UZS'
    usd = 'USD'


class Ad(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ads'
    )
    title = models.CharField(max_length=255)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='ads'
    )
    image = models.ImageField(upload_to='ads/', blank=True, null=True)

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField()
    view_count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    district = models.ForeignKey(District, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=255, choices=AdsStatus.choices, default=AdsStatus.new
    )
    bisnes_status = models.CharField(
        max_length=255, choices=BisnesStatus.choices, default=BisnesStatus.phisical
    )
    currency = models.CharField(
        max_length=255, choices=CurrencyChoise.choices, default=CurrencyChoise.uzs
    )

    is_top = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def update_view_count(self):
        self.view_count += 1
        self.save()
