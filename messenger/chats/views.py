# from django.shortcuts import render
from django.http import JsonResponse

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
        first = str(request.POST.get('first'))
        second = str(request.POST.get('second'))
        first_user = Chat.objects.filter(name=first)
        second_user = Chat.objects.filter(name=second).values('id')
        Chat.objects.create(name=first + ' with ' + second, tag='@' + first + second)
        new_chat = Chat.objects.filter(name=first + ' with ' + second)
        Member.objects.create(user_id=first_user, chat_id=new_chat)
        Member.objects.create(user_id=second_user, chat_id=new_chat)
        return HttpResponse
    else:
        return HttpResponseNotAllowed(['POST'])
