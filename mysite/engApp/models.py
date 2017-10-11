from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    word_pl = models.CharField(max_length=30)
    word_en = models.CharField(max_length=30)


class Section(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)


class Student(User):
    pass


class Profile(models.Model):
    id_student = models.ForeignKey(Student)
    level = models.CharField(max_length=2)