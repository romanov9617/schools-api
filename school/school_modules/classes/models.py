from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from school_modules.workers.models import Worker


class Class(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(
        validators=[MaxValueValidator(30), MinValueValidator(0)]
    )
    teacher = models.ForeignKey(Worker, on_delete=models.PROTECT)

    class Meta:
        db_table = "class"
