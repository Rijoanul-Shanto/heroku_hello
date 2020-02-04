from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from greetings.models import Greetings
from greetings.serializers import GreetingsSerializer


class HelloView(APIView):
    @staticmethod
    def get(request, name):
        data = {"name": name}
        serializer = GreetingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return HttpResponse("Hello " + name + "!", status=status.HTTP_201_CREATED)


class GreetingsView(APIView):
    @staticmethod
    def get(request):
        greetings = Greetings.objects.all()
        serializer = GreetingsSerializer(greetings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
