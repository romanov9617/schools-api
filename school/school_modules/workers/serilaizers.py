from rest_framework.serializers import ModelSerializer
from school_modules.workers.models import Worker


class WorkerSerilizer(ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
