# from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from chats.forms import *

@csrf_exempt
@require_GET
def chat_list(request):
    chats = Chat.objects.all().values('id', 'topic')
    return JsonResponse({'chats': list(chats)})

@csrf_exempt
@require_GET
def chat_detail(request, chatID):
    try:
        chat = Chat.objects.get(id=chatID)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')

    messages = Message.objects.filter(chat=chat).values('id', 'content', 'user', 'added_at')
    return JsonResponse({
        'Chat ID': chatID,
        'Messages': list(messages),
    })

@csrf_exempt
@require_POST
def create_chat(request):
    form = CreatePersonalChatForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Chat created'})
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def send_message(request):
    form = SendMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Message sended'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def read_message(request):
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Message read'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
