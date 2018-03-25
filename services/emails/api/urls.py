from django.urls import path
from . import views

# TODO: add here your API URLs

urlpatterns = [
	path("emails/send/", views.email_send)
]
