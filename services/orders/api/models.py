#from django.db import models #for sql
from djongo import models #for mongodb nosql

# TODO: write here your models


class Order(models.Model):
	total = models.FloatField()
	customer_name = models.CharField(max_length=100)
	customer_email = models.CharField(max_length=100)
	items = models.ListField(default=None)
