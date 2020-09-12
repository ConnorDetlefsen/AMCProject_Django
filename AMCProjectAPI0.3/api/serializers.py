from rest_framework import serializers
from .models import CorrectAnswer, CorrectAnswer2, AnswerList, AnswerList2, Question


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
        fields = ('id', 'question', 'question2', 'answerList', 'answerList2')
