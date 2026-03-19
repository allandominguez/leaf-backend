from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .api import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="list_users"),
    path("users/search/email/", views.UserSearchView.as_view(), name="search_email"),
    path("users/register/", views.UserCreateView.as_view(), name="create_user"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
