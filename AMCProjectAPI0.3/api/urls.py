from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CorrectAnswerViewSet, CorrectAnswer2ViewSet, AnswerListViewSet, AnswerList2ViewSet, QuestionViewSet, QuizResultsViewSet, UserViewSet, LoginTrackingViewSet, QuestionTrackingViewSet

router = routers.DefaultRouter()
router.register('correctAnswer', CorrectAnswerViewSet)
router.register('correctAnswer2', CorrectAnswer2ViewSet)
router.register('answerList', AnswerListViewSet)
router.register('answerList2', AnswerList2ViewSet)
router.register('question', QuestionViewSet)
router.register('users', UserViewSet)
router.register('logintracking', LoginTrackingViewSet)
router.register('questiontracking', QuestionTrackingViewSet)

router.register('quizResults', QuizResultsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
