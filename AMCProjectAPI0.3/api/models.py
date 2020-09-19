from django.db import models


# Create your models here.

class CorrectAnswer(models.Model):
    correctAnswer = models.TextField(max_length=364, null = True,blank = True)


class CorrectAnswer2(models.Model):
    correctAnswer2 = models.TextField(max_length=364, null = True,blank = True)


class AnswerList(models.Model):
    correctAnswer = models.OneToOneField(CorrectAnswer, blank=True, null=True, on_delete=models.CASCADE)
    answer1 = models.TextField(max_length=364, null = True, blank = True)
    answer2 = models.TextField(max_length=364, null = True, blank = True)
    answer3 = models.TextField(max_length=364, null = True, blank = True)
    answer4 = models.TextField(max_length=364, null = True, blank = True)


class AnswerList2(models.Model):
    correctAnswer2 = models.OneToOneField(CorrectAnswer2, blank=True, null=True, on_delete=models.CASCADE)
    answer1 = models.TextField(max_length=364, null = True, blank = True)
    answer2 = models.TextField(max_length=364, null = True, blank = True)
    answer3 = models.TextField(max_length=364, null = True, blank = True)
    answer4 = models.TextField(max_length=364, null = True, blank = True)


class Question(models.Model):
    QUESTIONTYPE = (
        ("MC", "Multiple Choice"),
        ('FREE', 'Free Response')
    )
    questionType = models.CharField(max_length=364, null=False, blank=False, default='', choices=QUESTIONTYPE)
    question = models.TextField(max_length=364, null=False)
    question2 = models.TextField(max_length=364, null=True)
    answerList = models.OneToOneField(AnswerList, blank=True, null=True, on_delete=models.CASCADE)
    answerList2 = models.OneToOneField(AnswerList2, blank=True, null=True, on_delete=models.CASCADE)


class QuizResults(models.Model):
    question1 = models.BooleanField(default = False)
    question2 = models.BooleanField(default = False)
    question3 = models.BooleanField(default = False)



class User(models.Model):
    username = models.CharField(max_length=364)
    password = models.CharField(max_length=356)
    quizResults = models.OneToOneField(QuizResults, blank=True, null=True, on_delete=models.CASCADE)
