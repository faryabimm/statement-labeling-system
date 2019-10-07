from enum import Enum

from django.db import models
from django.contrib.auth.models import User


class Statement(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class LabelChoices(Enum):
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'

    @staticmethod
    def values():
        return [(tag, tag.value) for tag in LabelChoices]

    @staticmethod
    def values_with_blank():
        return [('', '--------')] + LabelChoices.values()


class Label(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    answer_time = models.FloatField()
    label = models.CharField(
        max_length=8,
        choices=LabelChoices.values()
    )

    def __str__(self):
        return 'label: {label}, statement: {statement}'.format(label=self.label, statement=self.statement)
