from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ListSerializer
from .models import List


def welcome(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ListView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()