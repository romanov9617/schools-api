from rest_framework.serializers import ModelSerializer
from school_modules.core.serializers.mixins import OneEntityMixin
from school_modules.schools.models import School
from school_modules.workers.models import Worker
from school_modules.workers.serilaizers import WorkerSerializer


class SchoolSerilaizer(ModelSerializer):
    director = WorkerSerializer()

    def create(self, validated_data):
        director_data = validated_data.pop("director")
        director = Worker.objects.create(**director_data)
        school = School.objects.create(director=director, **validated_data)
        return school

    class Meta:
        model = School
        fields = "__all__"
        short_name = "school"


class OneSchoolSerilaizer(OneEntityMixin, SchoolSerilaizer):
    pass
