from email.policy import default
from django.core.validators import MaxValueValidator, MinValueValidator
from djongo import models

#Principal clases

class Asignature(models.Model):

    id = models.IntegerField(primary_key = True)
    term = models.CharField(max_length = 6)
    consolidated = models.BooleanField()


class History(models.Model):

    id = models.IntegerField(primary_key = True)
    id_student = models.CharField(max_length = 60)
    id_program = models.IntegerField(default = 0)
    percentage_adv = models.FloatField()
    asignature_taken = models.JSONField(default=[])


class Grade(models.Model):

    id = models.IntegerField(primary_key = True)
    id_asignature = models.IntegerField(default=0)
    name = models.CharField(max_length = 60)
    percentage = models.FloatField()
    id_students = models.CharField(max_length = 60)
    values = models.FloatField(default = 0)



