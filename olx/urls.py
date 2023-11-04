from django.urls import path

from .views import CategoryView, SubCategoryView, AdView, AdsView, AdCreateView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('subcategory/', SubCategoryView.as_view()),
    path('ad/', AdsView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/', AdView.as_view())
]
