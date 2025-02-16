from django.urls import path
from .views import legal_entity_form, profile, send_verification_email, verify_email

urlpatterns = [
    path('', profile, name='profile'),
    path('legal-entity/', legal_entity_form, name='legal_entity_form'),
    path('send-verification-email/', send_verification_email, name='send_verification_email'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
]