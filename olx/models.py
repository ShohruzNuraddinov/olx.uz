from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel
# Create your models here.


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BisnesStatus(models.Choices):
    phisical = 'Jismoniy'
    biznes = 'Biznes'


class AdsStatus(models.Choices):
    new = 'Yangi'
    fb = 'F/B'


class Ads(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=True)

    description = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    status = models.CharField(
        max_length=255, choices=AdsStatus.choices, default=AdsStatus.new)
    bisnes_status = models.CharField(
        max_length=255, choices=BisnesStatus.choices, default=BisnesStatus.phisical)

    def __str__(self) -> str:
        return self.title
