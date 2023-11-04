from django.shortcuts import render
from django.db import models
from django.db.models.functions import Coalesce
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


from .serailizers import CategorySerailizer, SubCategorySerailizer, AdSerailizer, AdCreateSerailizer
from .models import Category, SubCategory, Ad, Brand
from utils.paginations import StandardResultsSetPagination
# Create your views here.


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.annotate(
        ads_count=Coalesce(
            models.Count(models.F('sub_categories__ads')), 0
        )
    )
    serializer_class = CategorySerailizer


class SubCategoryView(generics.ListAPIView):
    queryset = SubCategory.objects.annotate(
        ads_count=Coalesce(models.Count(models.F('ads')), 0))
    serializer_class = SubCategorySerailizer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']


class AdsView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerailizer
    pagination_class = StandardResultsSetPagination


class AdView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerailizer

    def get(self, request, pk):
        ad = Ad.objects.get(id=pk)
        ad.update_view_count()
        serailizer = AdSerailizer(ad)
        return Response(serailizer.data)


class AdCreateView(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerailizer
    permission_classes = [IsAuthenticated]
