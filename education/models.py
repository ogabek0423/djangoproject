from django.db import models

from django.db import models


class Edu(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()


class Pupil(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Edu_pupil(models.Model):
    book_id = models.ForeignKey(Edu, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    talked_date = models.DateTimeField()
