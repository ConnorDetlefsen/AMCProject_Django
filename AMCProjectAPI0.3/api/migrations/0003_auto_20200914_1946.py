# Generated by Django 3.1.1 on 2020-09-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_question_questiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerlist2',
            name='answer1',
            field=models.TextField(max_length=364, null=True),
        ),
    ]
