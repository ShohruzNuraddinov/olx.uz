from rest_framework import serializers

from .models import Ad, Category, SubCategory, Brand


class CategorySerailizer(serializers.ModelSerializer):
    ads_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = [
            'title',
            'ads_count'
        ]


class SubCategorySerailizer(serializers.ModelSerializer):
    ads_count = serializers.IntegerField()
    category = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='title'
    )

    class Meta:
        model = SubCategory
        fields = [
            'title',
            'category',
            'ads_count'
        ]


class AdSerailizer(serializers.ModelSerializer):
    # image = serializers.ImageField(url=True)
    sub_category = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='title'
    )
    district = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='title'
    )
    brand = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='title'
    )
    # sub_category = SubCategory()

    class Meta:
        model = Ad
        fields = [
            'id',
            'title',
            'image',
            'sub_category',
            'brand',
            'description',
            'district',
            'view_count',
            'status',
            'bisnes_status',
            'currency',
            'is_top'
        ]


class AdCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'title',
            'image',
            'sub_category',
            'brand',
            'description',
            'district',
            'view_count',
            'status',
            'bisnes_status',
            'currency',
            'is_top',
        ]
