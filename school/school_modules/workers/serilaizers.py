from rest_framework.serializers import ModelSerializer
from school_modules.core.serializers.mixins import OneEntityMixin
from school_modules.workers.models import Worker


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
        short_name = "worker"


class OneWorkerSerializer(OneEntityMixin, WorkerSerializer):
    pass
