from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Booking_book(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    talked_date = models.DateTimeField()
