from django.urls import path
from .views import education_view

urlpatterns = [
    path("education/", education_view, name="education"),
]