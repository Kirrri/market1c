from django.urls import path
from .views import legal_entity_form, profile

urlpatterns = [
    path('', profile, name='profile'),
    path('legal-entity/', legal_entity_form, name='legal_entity_form'),
]