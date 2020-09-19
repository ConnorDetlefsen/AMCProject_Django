from django.contrib import admin
from .models import CorrectAnswer, CorrectAnswer2, AnswerList, AnswerList2, Question, QuizResults, User
# Register your models here.

admin.site.register(CorrectAnswer)
admin.site.register(CorrectAnswer2)

admin.site.register(AnswerList)
admin.site.register(AnswerList2)

admin.site.register(Question)
admin.site.register(User)
admin.site.register(QuizResults)