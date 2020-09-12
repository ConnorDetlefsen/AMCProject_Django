from django.shortcuts import render
from rest_framework import viewsets
from .models import CorrectAnswer, CorrectAnswer2, AnswerList, AnswerList2, Question
from .serializers import CorrectAnswerSerializer,CorrectAnswer2Serializer, AnswerListSerializer,AnswerList2Serializer, QuestionSerializer


# Create your views here.

class CorrectAnswerViewSet(viewsets.ModelViewSet):
    queryset = CorrectAnswer.objects.all()
    serializer_class = CorrectAnswerSerializer

class CorrectAnswer2ViewSet(viewsets.ModelViewSet):
    queryset = CorrectAnswer2.objects.all()
    serializer_class = CorrectAnswer2Serializer


class AnswerListViewSet(viewsets.ModelViewSet):
    queryset = AnswerList.objects.all()
    serializer_class = AnswerListSerializer

class AnswerList2ViewSet(viewsets.ModelViewSet):
    queryset = AnswerList2.objects.all()
    serializer_class = AnswerList2Serializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
