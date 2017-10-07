from __future__ import unicode_literals

from django.db import models


class Camper(models.Model):
    AGE_CHOICES = (
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (16, "16"),
        (17, "17"),
        (18, "18"),

    )
    SINGER= "singer"
    GUITARIST = "guitarist"
    DRUMMER ="drummer"
    BASSIST = "bassist"
    KEYBOARDIST= "keyboardist"
    INSTRUMENTALIST= "instrumentalist"

    CATEGORY_CHOICES = (
        (SINGER, "Singer"),
        (GUITARIST, "Guitarist"),
        (DRUMMER, "Drummer"),
        (BASSIST, "Bassist"),
        (KEYBOARDIST, "Keyboardist"),
        (INSTRUMENTALIST, "Instrumentalist"),

    )
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', "Female"),
    )
    RANK_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
    )

    name = models.CharField(max_length=200)
    age = models.BigIntegerField(choices=AGE_CHOICES)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    rank = models.BigIntegerField(choices=RANK_CHOICES)

class Dorm(models.Model):
    name=models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=10,choices=Camper.GENDER_CHOICES)
    camper = models.ManyToManyField(Camper,null=True,blank=True)
    young_count = models.BigIntegerField(default=0)
    middle_count = models.BigIntegerField(default=0)
    old_count = models.BigIntegerField(default=0)

class Band(models.Model):
    name=models.CharField(max_length=100,default='')
    camper = models.ManyToManyField(Camper,null=True,blank=True)
    boys_count = models.BigIntegerField(default=0)
    girls_count = models.BigIntegerField(default=0)

