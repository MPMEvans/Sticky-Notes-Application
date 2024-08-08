# bulleting_board/urls.py
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the entire project
urlpatterns = [
    # Admin URL pattern, mapping to the Django admin interface
    path("admin/", admin.site.urls),
    # Include URL patterns from the 'posts' app
    # All URLS from 'posts.urls' will be prefixed with 'posts/'
    path("", include("posts.urls")),
]
