from rest_framework.views import APIView
from .models import Category, Product
import json
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET", "POST"])
def categories(request):
	if not request.META["HTTP_AUTH_ID"] or request.META["HTTP_AUTH_ID"] != "MY155":
		return Response({"message": "Authorization Failed"})

	if request.method == "POST":
		new_cat = Category.objects.create(name=request.data["category_name"])
	categories_lst = Category.objects.all()
	srlz = CategorySerializer(categories_lst, many=True)
	return Response(srlz.data)


@api_view(http_method_names=["GET"])
def products_fetch(request):
	if request.query_params.get("cat_id"):
		products_list = Product.objects.filter(category__id=request.query_params.get("cat_id"))
	elif request.query_params.get("prod_id"):
		products_list = Product.objects.filter(id=request.query_params.get("prod_id"))
	else:
		products_list = Product.objects.all()
	if products_list:
		srlz = ProductSerializer(products_list, many=True)
		return Response(srlz.data, status=200)
	else:
		return Response({"message": "Sorry not found!"}, status=404)


@api_view(http_method_names=["POST"])
def products_create(request):
	new_prod = Product.objects.create(
		category=request.data["cat_id"],
		name=request.data["prod_name"],
		price=request.data["prod_price"],
		description=request.data["prod_description"],
	)
	return Response({"message": "Product added successfully"}, status=300)


@api_view(http_method_names=["DELETE"])
def products_delete(request):
	if not request.data["prod_id"]:
		return Response({"message": "Sorry not found!"}, status=500)
	product = Product.objects.get(id=request.data["prod_id"])
	product.delete()
	return Response({"message": "Product deleted successfully"}, status=300)
