from django.db import models
from django.db.models.functions import Coalesce

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    balance = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.get_full_name()
