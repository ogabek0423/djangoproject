from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    create_time = models.DateTimeField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salary = models.FloatField()


class Subject(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    modules = models.IntegerField()


class Teach_specs(models.Model):
    teach_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    spec_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    dates = models.DateTimeField()


class Teach_subject(models.Model):
    teach_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    dates = models.DateTimeField()

