from chats.views import chat_list, chat_detail
from django.urls import path, include

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chatID>', chat_detail, name='chat_detail'),
]