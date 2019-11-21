# from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from chats.models import Chat, Member
from users.models import User

def get_chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all()
        return JsonResponse({'chats': list(chats)})
    else:
        return HttpResponseNotAllowed(['GET'])

def chat_detail(request, chatID):
    if request.method == 'GET':
        return JsonResponse( { 'test': 'Chat window', 'chatID': chatID} )
    else:
        raise HttpResponseNotAllowed(['GET'])

def create_chat(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        user = Chat.objects.filter(name=username)

        chat = Chat.objects.create(topic=user.username, is_group_chat=False)
        Member.objects.create(user=user.id, chat=chat.id)
        return HttpResponse
    else:
        return HttpResponseNotAllowed(['POST'])
