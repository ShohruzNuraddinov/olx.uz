from django.contrib import admin

from django.apps import apps
from user.models import UserModel
# Register your models here.

for model in apps.get_models():
    if UserModel != model:
        try:

            admin.site.register(model)
        except:
            pass
