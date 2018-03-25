from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from .models import Email
from rest_framework.response import Response
from rest_framework.decorators import api_view

# TODO: add here your API Views

@api_view(http_method_names=["POST"])
def email_send(request):
	sender = settings.EMAIL_HOST_USER
	try:
		receiver = request.data["receiver"]
		subject = request.data["subject"]
		body = request.data["body"]

		new_mail = Email.objects.create(
			sender=sender,
			receiver=receiver,
			subject=subject,
			body=body
		)

		send_mail(subject, body, sender, [receiver], fail_silently=False)
		return Response({"message": "Email sent successfully"}, status=200)

	except:
		return Response({"message": "Email sending error"}, status=500)






