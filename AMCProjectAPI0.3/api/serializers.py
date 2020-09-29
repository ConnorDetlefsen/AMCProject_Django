from rest_framework import serializers
from .models import CorrectAnswer, CorrectAnswer2, AnswerList, AnswerList2, Question, QuizResults, User, LoginTracking, QuestionTracking

class CorrectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectAnswer
        fields = ('id', 'correctAnswer')


class CorrectAnswer2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectAnswer2
        fields = ('id', 'correctAnswer2')


class AnswerListSerializer(serializers.ModelSerializer):
    correctAnswer = CorrectAnswerSerializer(many=False)

    class Meta:
        model = AnswerList
        fields = ('id', 'answer1', 'answer2', 'answer3', 'answer4', 'correctAnswer')


class AnswerList2Serializer(serializers.ModelSerializer):
    correctAnswer2 = CorrectAnswer2Serializer(many=False)

    class Meta:
        model = AnswerList2
        fields = ('id', 'answer1', 'answer2', 'answer3', 'answer4', 'correctAnswer2')


class QuestionSerializer(serializers.ModelSerializer):
    answerList = AnswerListSerializer(many=False)
    answerList2 = AnswerList2Serializer(many=False)

    class Meta:
        model = Question
        fields = ('id', 'questionType', 'question', 'question2', 'answerList', 'answerList2')



class QuizResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizResults
        fields = ('id', 'question1', 'question2', 'question3', 'question4')


class UserSerializer(serializers.ModelSerializer):
    quizResults = QuizResultsSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'currentQuestion', 'quizResults')


class LoginTrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginTracking
        fields = ('login_id', 'user_id', 'stamp')


class QuestionTrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionTracking
        fields = ('id', 'user_id', 'stamp', 'question', 'answer', 'correct')