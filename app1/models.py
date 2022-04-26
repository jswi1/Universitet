from django.db import models

class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    daraja = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.ism


class Fan(models.Model):
    nom = models.CharField(max_length=30)
    yonalish = models.ManyToManyField('app1.Ustoz',related_name='ustozlar')
    def __str__(self):
        return self.nom


class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    code = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    is_active = models.BooleanField()
    def __str__(self):
        return self.nom



