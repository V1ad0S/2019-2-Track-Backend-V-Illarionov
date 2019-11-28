from chats.views import chat_list, chat_detail, send_message, read_message, create_chat
from django.urls import path, include

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chatID>', chat_detail, name='chat_detail'),
    path('create_chat/', create_chat, name='create_chat'),
    path('send_message/', send_message, name='send_message'),
    path('read_message/', read_message, name='read_message'),
]
