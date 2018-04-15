from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200)
    time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    max_mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    questions_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)])

    def __str__(self):
        return self.title


class QuestionType(models.Model):
    CHOICES = (
        ('single', 'Single'),
        ('multiple', 'Multiple'),
    )
    type = models.CharField(max_length=20, choices=CHOICES, default='single')

    def __str__(self):
        return self.type


class Question(models.Model):
    question = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    TYPES = (
        ('correct', 'Correct'),
        ('wrong', 'Wrong'),
    )
    type = models.CharField(max_length=20, choices=TYPES, default='wrong')
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
