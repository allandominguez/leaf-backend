from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .api import views

urlpatterns = [
    path("users/", views.UserListView.as_view()),
    path("users/search/email/", views.UserSearchView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
