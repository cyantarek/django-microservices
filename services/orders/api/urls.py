from django.urls import path
from . import views

# TODO: add here your API URLs

urlpatterns = [
	path("orders/add/", views.add_order)
]
