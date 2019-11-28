from users.views import get_profile, contact_list, find_users
from django.urls import path, include

urlpatterns = [
    path('', get_profile, name='get_profile'),
    path('contacts/', contact_list, name='contact_list'),
    path('find_users/', find_users, name='find_users'),
]
