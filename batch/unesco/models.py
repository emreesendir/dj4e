from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self) :
        return self.name


class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=600, null=True)
    justification = models.CharField(max_length=600, null=True)
    year = models.IntegerField(null=True)
    longtitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True)
    iso = models.ForeignKey(Iso, on_delete=models.DO_NOTHING, null=True)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) :
        return self.name

