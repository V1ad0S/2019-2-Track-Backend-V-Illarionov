# from django.shortcuts import render
from django.http import JsonResponse


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
        user = User.objects.filter(name__contains=request.GET.get('name'))
        return HttpResponse
    else:
        return HttpResponseNotAllowed(['GET'])
