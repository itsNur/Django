from django.db import models


class Command(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=100)
    command = models.ForeignKey(Command, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
