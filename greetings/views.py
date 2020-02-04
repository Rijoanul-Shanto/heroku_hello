from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


class HelloView(APIView):
    @staticmethod
    def get(request, name):
        return HttpResponse("Hello " + name + "!")


class GreetingsView(APIView):
    pass
