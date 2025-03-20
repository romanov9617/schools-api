from rest_framework.serializers import ModelSerializer
from school_modules.classes.models import Class
from school_modules.core.serializers.mixins import OneEntityMixin
from school_modules.workers.serilaizers import WorkerSerializer


class ClassSerializer(ModelSerializer):
    teacher = WorkerSerializer()

    class Meta:
        model = Class
        fields = "__all__"


class OneClassSerializer(OneEntityMixin, ClassSerializer):
    pass
