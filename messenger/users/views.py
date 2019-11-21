# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from users.models import User


def get_profile(request):
    if request.method == 'GET':
        return JsonResponse( { 'test': 'Profile' } )
    else:
        raise HttpResponseNotAllowed(['GET'])

def contact_list(request):
    if request.method == 'GET':
        return JsonResponse( { 'test': 'Contact list' } )
    else:
        raise HttpResponseNotAllowed(['GET'])

def find_users(request):
    if request.method == 'GET':
        user = User.objects.filter(username__contains=request.GET.get('name'))
        return HttpResponse
    else:
        return HttpResponseNotAllowed(['GET'])
