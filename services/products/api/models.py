from djongo import models #for mongodb nosql

# TODO: write here your models

class Category(models.Model):
	name = models.CharField(max_length=100)


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()
