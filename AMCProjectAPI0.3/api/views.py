from django.shortcuts import render
from rest_framework import viewsets
from .models import CorrectAnswer, CorrectAnswer2, AnswerList, AnswerList2, Question, QuizResults, User, LoginTracking, QuestionTracking
from .serializers import CorrectAnswerSerializer,CorrectAnswer2Serializer, AnswerListSerializer,AnswerList2Serializer, QuestionSerializer, QuizResultsSerializer, UserSerializer, LoginTrackingSerializer, QuestionTrackingSerializer


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


class QuizResultsViewSet(viewsets.ModelViewSet):
    queryset = QuizResults.objects.all()
    serializer_class = QuizResultsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginTrackingViewSet(viewsets.ModelViewSet):
    queryset = LoginTracking.objects.all()
    serializer_class = LoginTrackingSerializer


class QuestionTrackingViewSet(viewsets.ModelViewSet):
    queryset = QuestionTracking.objects.all()
    serializer_class = QuestionTrackingSerializer