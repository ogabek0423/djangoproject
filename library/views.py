from django.shortcuts import render
from .models import Book, Student, Booking_book

def library_views(request):
    return render(request, "library/library.html")


def book_view(request):
    books = Book.objects.all()
    return render(request, "library/book_view.html", {"books": books})


