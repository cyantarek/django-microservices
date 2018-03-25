#from django.db import models #for sql
from djongo import models #for mongodb nosql

# TODO: write here your models

class Email(models.Model):
	sender = models.EmailField()
	receiver = models.EmailField()
	subject = models.CharField(max_length=300)
	body = models.TextField()
