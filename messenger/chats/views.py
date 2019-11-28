# from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from chats.forms import *

@csrf_exempt
@require_GET
def chat_list(request):
    user_id = request.GET.get('user_id')
    chat_id_list = [member.chat_id for member in Member.objects.filter(user=user_id)]
    return JsonResponse({'chat_id_list': chat_id_list})

@csrf_exempt
@require_GET
def chat_detail(request, chatID):
    try:
        chat = Chat.objects.get(id=chatID)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')

    message_id_list = [message.id for message in Message.objects.filter(chat=chat).order_by('-added_at')]
    return JsonResponse({
        'Messages': message_id_list,
    })

@csrf_exempt
@require_POST
def create_chat(request):
    form = CreatePersonalChatForm(request.POST)
    if form.is_valid():
        chat_id = form.save()
        return JsonResponse({'chat_id': chat_id})
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def send_message(request):
    form = SendMessageForm(request.POST)
    if form.is_valid():
        message_id = form.save()
        return JsonResponse({'message_id': message_id})
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
