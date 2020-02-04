from django.urls import path, include

from greetings.views import HelloView, GreetingsView

urlpatterns = [
    path('hello/<str:name>', HelloView.as_view()),
    path('greetings/', GreetingsView.as_view()),
]
