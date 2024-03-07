from django.urls import path
from .views import library_views, book_view


urlpatterns = [
    path("library/", library_views, name='library'),
    path("", book_view, name='books')
]
