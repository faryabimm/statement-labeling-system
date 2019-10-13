from enum import Enum

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Statement(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class LabelChoices(Enum):
    POSITIVE = ('Positive', '+')
    NEGATIVE = ('Negative', '-')
    NEUTRAL = ('Neutral', '=')
    UNCERTAIN = ('Vague', '?')

    @staticmethod
    def values():
        return [(tag, tag.value[0]) for tag in LabelChoices]

    @staticmethod
    def values_with_blank():
        return [('', '--------')] + LabelChoices.values()

    def __str__(self):
        return self.value[0]

    def sign(self):
        return self.value[1]

    @staticmethod
    def value_of(string):
        for tag in LabelChoices:
            if tag.value[0] == string:
                return tag
        return None


class Label(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    answer_time = models.FloatField()
    label = models.CharField(
        max_length=8,
        choices=LabelChoices.values()
    )

    def __str__(self):
        return '{label} {time}s [{user}] {statement}'.format(
            label='({})'.format(LabelChoices.value_of(self.label).sign()),
            time=round(self.answer_time, settings.ADMIN_STATEMENT_RESPONSE_TIME_PRECISION),
            user=self.user.username,
            statement=self.statement.text[:settings.ADMIN_STATEMENT_PREVIEW_CHARACTER_LIMIT] + '...',
        )
