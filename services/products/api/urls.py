from django.urls import path
from . import views

# TODO: add here your API URLs

urlpatterns = [
	path("private/categories/", views.categories),
	path("products/fetch/", views.products_fetch),
	path("products/create/", views.products_create),
	path("products/delete/", views.products_delete),
]
