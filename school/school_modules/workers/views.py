from rest_framework.viewsets import ModelViewSet
from school_modules.workers.models import Worker
from school_modules.workers.serilaizers import WorkerSerilizer


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerilizer
