from django.db import models

from django.db import models


class Edu(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Pupil(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.group_name}'


class Edu_pupil(models.Model):
    book_id = models.ManyToManyField(Edu)
    student_id = models.ManyToManyField(Pupil)
    talked_date = models.DateTimeField()

    def __str__(self):
        return f'{self.book_id} - {self.student_id}'


