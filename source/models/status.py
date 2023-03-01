from django.db.models import TextChoices
from django.db import models


class StatusChoice(TextChoices):
    NEW = 'NEW', 'New'
    IN_PROGRESS = 'IN_PROGRESS', 'In progress'
    DONE = 'DONE', 'Done'


class Status(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Status'
    )

    def __str__(self):
        return self.name
