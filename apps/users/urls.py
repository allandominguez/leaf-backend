from django.urls import path
from .api import views

urlpatterns = [
    path("users/", views.UserListView.as_view()),
    path("users/search/", views.UserSearchView.as_view()),
]