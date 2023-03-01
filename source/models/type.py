from django.db.models import TextChoices
from django.db import models


class TypeChoice(TextChoices):
    TASK = 'TASK', 'Task'
    BUG = 'BUG', 'Bug'
    ENHANCEMENT = 'ENHANCEMENT', 'Enhancement'


class Type(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Type'
    )

    def __str__(self):
        return self.name
