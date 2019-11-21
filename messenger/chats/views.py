# from django.shortcuts import render
from django.http import JsonResponse

def chat_list(request):
    if request.method == 'GET':
        return JsonResponse( { 'test': 'Chat list' } )
    else:
        raise HttpResponseNotAllowed(['GET'])

def chat_detail(request, chatID):
    if request.method == 'GET':
        return JsonResponse( { 'test': 'Chat window', 'chatID': chatID} )
    else:
        raise HttpResponseNotAllowed(['GET'])
