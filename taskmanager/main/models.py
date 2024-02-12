from django.db import models


class Command(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=100)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
