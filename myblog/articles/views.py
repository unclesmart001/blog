from django.http import HttpResponse
from django.shortcuts import render


def article(request):
    return HttpResponse('view my articles')