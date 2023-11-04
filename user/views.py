from django.shortcuts import render
from django.db import models
from django.db.models.functions import Coalesce

from rest_framework import generics

from .models import UserModel as User
from .serailizers import UserSeralizer, UserBalanceSerailizer
# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.annotate(
        ads_count=Coalesce(models.Count(models.F('ads')), 0)
    )
    serializer_class = UserSeralizer


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.annotate(
        ads_count=Coalesce(models.Count(models.F('ads')), 0)
    )
    serializer_class = UserSeralizer


class UserBalanceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserBalanceSerailizer
