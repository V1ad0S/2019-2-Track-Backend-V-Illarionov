from users.views import get_profile, contact_list
from django.urls import path, include

urlpatterns = [
    path('', get_profile, name='get_profile'),
    path('contacts', contact_list, name='contact_list'),
]