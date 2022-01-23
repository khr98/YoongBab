from django.db import models

# Create your models here.
class ChaSeDae(models.Model):
    moms = models.TextField(verbose_name="맘스",null=True)
    chef = models.TextField(verbose_name="셰프",null=True)
    special = models.TextField(verbose_name="정찬",null=True)
    salad = models.TextField(verbose_name="샐러드",null=True)
    dinner = models.TextField(verbose_name="석식",null=True)
    takeOut = models.TextField(verbose_name="TakeOut",null=True)
    date = models.DateField(verbose_name="날짜", null=True)
    
class Nano(models.Model):
    lunchA = models.TextField(verbose_name="코스A", null=True)
    lunchB = models.TextField(verbose_name="코스B", null=True)
    plus = models.TextField(verbose_name="PLUS", null=True)
    dinner = models.TextField(verbose_name="저녁", null=True)
    date = models.DateField(verbose_name="날짜", null=True)

class RDB(models.Model):
    korea = models.TextField(verbose_name="한식", null=True)
    special = models.TextField(verbose_name="일품", null=True)
    plus = models.TextField(verbose_name="플러스바", null=True)
    dinner = models.TextField(verbose_name="저녁", null=True)
    takeOut = models.TextField(verbose_name="TakeOut",null=True)
    date = models.DateField(verbose_name="날짜", null=True)