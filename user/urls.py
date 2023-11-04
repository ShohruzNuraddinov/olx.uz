from django.urls import path

from .views import UserListView, UserView, UserBalanceUpdateView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserView.as_view()),
    path('<int:pk>/update/', UserBalanceUpdateView.as_view())
]
