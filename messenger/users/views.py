# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from users.models import User


@csrf_exempt
@require_GET
def get_profile(request):
    try:
        user = User.objects.get(id=request.GET.get('id'))
    except User.DoesNotExist:
        return HttpResponse('No such user')
    return JsonResponse({'username':user.username})

@csrf_exempt
@require_GET
def contact_list(request):
    users = User.objects.all().values('id', 'username')
    return JsonResponse({'users': list(users)})

@csrf_exempt
@require_GET
def find_users(request):
    users = list(User.objects.filter(username__contains=request.GET.get('username')).values('id', 'username'))
    return JsonResponse({'users': users})
