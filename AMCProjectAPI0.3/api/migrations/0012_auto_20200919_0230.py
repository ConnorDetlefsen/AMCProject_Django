# Generated by Django 3.1.1 on 2020-09-19 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizresults',
            old_name='questionAnswer',
            new_name='question1',
        ),
        migrations.AddField(
            model_name='quizresults',
            name='question2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quizresults',
            name='question3',
            field=models.BooleanField(default=False),
        ),
    ]
