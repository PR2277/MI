# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Weather(models.Model):
	tem_value=models.CharField(max_length=250)
	hum_value=models.CharField(max_length=250)
        soil_value=models.CharField(max_length=250)
        rain_value=models.CharField(max_length=250)
        water_value=models.CharField(max_length=250)
        motor_value=models.CharField(max_length=250)
class Weather1(models.Model):
	tem_value1=models.CharField(max_length=250)
	hum_value1=models.CharField(max_length=250)
        soil_value1=models.CharField(max_length=250)
        rain_value1=models.CharField(max_length=250)
        water_value1=models.CharField(max_length=250)
        motor_value1=models.CharField(max_length=250)

