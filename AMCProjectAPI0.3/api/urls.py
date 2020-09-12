from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CorrectAnswerViewSet, CorrectAnswer2ViewSet, AnswerListViewSet, AnswerList2ViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register('correctAnswer', CorrectAnswerViewSet)
router.register('correctAnswer2', CorrectAnswer2ViewSet)
router.register('answerList', AnswerListViewSet)
router.register('answerList2', AnswerList2ViewSet)
router.register('question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
