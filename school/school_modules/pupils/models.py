from django.db import models
from school_modules.classes.models import Class


class Pupil(models.Model):
    fio = models.CharField(max_length=100)
    birth_date = models.DateField()
    _class = models.ForeignKey(Class, on_delete=models.PROTECT, db_column="class")

    class Meta:
        db_table = "pupil"
