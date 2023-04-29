from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
# Create your views here.
from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
