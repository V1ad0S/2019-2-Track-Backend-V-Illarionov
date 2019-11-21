from django.http import HttpResponseNotAllowed
from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponseNotAllowed(['GET'])
