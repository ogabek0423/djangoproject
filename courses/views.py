from django.shortcuts import render


def courses_view(request):
    return render(request, "courses/course.html")

