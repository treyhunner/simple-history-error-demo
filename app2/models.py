from django.db import models
from simple_history.models import HistoricalRecords


class Model1(models.Model):
    history = HistoricalRecords()


class Model2(models.Model):
    text = models.TextField()
