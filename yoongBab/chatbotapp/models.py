from django.db import models

# Create your models here.
class ChaSeDae(models.Model):
    moms = models.TextField(verbose_name="맘스")
    chef = models.TextField(verbose_name="셰프")
    special = models.TextField(verbose_name="정찬")
    salad = models.TextField(verbose_name="샐러드")