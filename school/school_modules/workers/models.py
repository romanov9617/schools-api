from django.db import models


class Worker(models.Model):
    fio = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        db_table = "worker"
