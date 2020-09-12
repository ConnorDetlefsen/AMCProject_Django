from django.db import models

# Create your models here.

class CorrectAnswer(models.Model):
    correctAnswer = models.TextField(max_length=364)


class CorrectAnswer2(models.Model):
    correctAnswer2 = models.TextField(max_length=364)


class AnswerList(models.Model):
    correctAnswer = models.OneToOneField(CorrectAnswer, blank=True, null=True, on_delete=models.CASCADE)
    answer1 = models.TextField(max_length=364)
    answer2 = models.TextField(max_length=364)
    answer3 = models.TextField(max_length=364)
    answer4 = models.TextField(max_length=364)


class AnswerList2(models.Model):
    correctAnswer2 = models.OneToOneField(CorrectAnswer2, blank=True, null=True, on_delete=models.CASCADE)
    answer1 = models.TextField(max_length=364)
    answer2 = models.TextField(max_length=364)
    answer3 = models.TextField(max_length=364)
    answer4 = models.TextField(max_length=364)


class Question(models.Model):
    question = models.TextField(max_length=364, null=False)
    question2 = models.TextField(max_length=364, null=True)
    answerList = models.OneToOneField(AnswerList, blank=True, null=True, on_delete=models.CASCADE)
    answerList2 = models.OneToOneField(AnswerList2, blank=True, null=True, on_delete=models.CASCADE)
