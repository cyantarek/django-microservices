from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Order


# TODO: add here your API Views

@api_view(http_method_names=["POST"])
def add_order(request):
	total_price = 0
	order = Order()
	order.customer_name = request.data["customer_name"]
	order.customer_email = request.data["customer_email"]
	order.items = []

	print(request.data)

	for product in request.data["products_id"]:
		response = requests.get("http://127.0.0.1:8001/products/fetch/?prod_id=%s" % product).json()
		print(response)
		total_price += float(response[0]["price"])

		order.items.append({
			"item_name": response[0]["name"],
			"item_description": response[0]["description"],
			"item_price": response[0]["price"],
		})
	order.total = total_price
	order.save()

	# send_email.delay(order)
	send_email(order)

	return Response({"message": "Order successfully created!"})


def send_email(order):
	requests.post("http://127.0.0.1/api/v1/emails/send/", data={
		"receiver": order.customer_email,
		"subject": "Order Created",
		"body": "Hello %s, your order has been created. Total of: %s. Thanks" % (order.customer_name, order.total)
	})
