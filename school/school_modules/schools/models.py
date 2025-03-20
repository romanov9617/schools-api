from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from school_modules.workers.models import Worker


class School(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MaxValueValidator(2024), MinValueValidator(1400)]
    )
    director = models.ForeignKey(Worker, on_delete=models.PROTECT)
    raiting = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )

    class Meta:
        db_table = "school"
