from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')


urlpatterns = [
	path("private/categories/", views.categories),
	path("products/fetch/", views.products_fetch),
	path("products/create/", views.products_create),
	path("products/delete/", views.products_delete),
	path("products/docs/", schema_view),
]
