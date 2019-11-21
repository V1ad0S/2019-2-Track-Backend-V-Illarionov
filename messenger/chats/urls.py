from chats.views import get_chat_list, chat_detail
from django.urls import path, include

urlpatterns = [
    path('', get_chat_list, name='chat_list'),
    path('<int:chatID>', chat_detail, name='chat_detail'),
]