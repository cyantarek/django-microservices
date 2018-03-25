from rest_framework import serializers

from .models import Category, Product

# TODO: write here your model serializers

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = [
			"id",
			"name"
		]

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"
