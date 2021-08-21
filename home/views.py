from django.http import JsonResponse
from django.shortcuts import render

import json


def index(request):
    return render(request, 'home/index.html', {

    })
